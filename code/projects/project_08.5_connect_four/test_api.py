"""
Tests for Connect Four web API endpoints.

Run from Study root:
    PYTHONPATH="code:$PYTHONPATH" python -m pytest code/projects/project_08.5_connect_four/test_api.py -v
"""

import pytest
import sys
import os

# Add paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from web_app import app


@pytest.fixture
def client():
    """Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestNewGameAPI:
    """Tests for /api/new-game endpoint."""

    def test_new_game_default(self, client):
        """Test new game with default settings."""
        response = client.post('/api/new-game',
                              json={})
        assert response.status_code == 200

        data = response.get_json()
        assert 'board' in data
        assert 'current_player' in data
        assert 'legal_moves' in data
        assert 'rows' in data
        assert 'cols' in data

        assert len(data['board']) == 42  # 6×7
        assert data['current_player'] in [1, -1]
        assert data['rows'] == 6
        assert data['cols'] == 7

    def test_new_game_custom_size(self, client):
        """Test new game with custom board size."""
        response = client.post('/api/new-game',
                              json={'rows': 5, 'cols': 6})
        assert response.status_code == 200

        data = response.get_json()
        assert len(data['board']) == 30  # 5×6
        assert data['rows'] == 5
        assert data['cols'] == 6

    def test_new_game_ai_first(self, client):
        """Test new game with AI playing first."""
        response = client.post('/api/new-game',
                              json={'ai_first': True})
        assert response.status_code == 200

        data = response.get_json()
        # Board should have 1 piece (AI's first move)
        assert sum(1 for x in data['board'] if x != 0) == 1

    def test_new_game_custom_simulations(self, client):
        """Test new game with custom MCTS simulations."""
        response = client.post('/api/new-game',
                              json={'num_simulations': 500})
        assert response.status_code == 200

        data = response.get_json()
        assert 'board' in data


class TestMakeMoveAPI:
    """Tests for /api/make-move endpoint."""

    def test_make_move_valid(self, client):
        """Test making a valid move."""
        # Start new game
        client.post('/api/new-game', json={})

        # Make move in column 3 (d)
        response = client.post('/api/make-move',
                              json={'column': 3})
        assert response.status_code == 200

        data = response.get_json()
        assert 'board' in data
        assert 'current_player' in data
        assert 'legal_moves' in data
        assert 'is_terminal' in data
        assert 'move_row' in data

        # Check that piece was placed
        assert sum(1 for x in data['board'] if x != 0) == 1

        # Check row where piece landed (should be row 0, bottom)
        assert data['move_row'] == 0

    def test_make_move_invalid_column(self, client):
        """Test making move in invalid column."""
        # Start new game
        client.post('/api/new-game', json={})

        # Try invalid column
        response = client.post('/api/make-move',
                              json={'column': 10})
        assert response.status_code == 400

        data = response.get_json()
        assert 'error' in data

    def test_make_move_full_column(self, client):
        """Test making move in full column."""
        # Start new game
        client.post('/api/new-game', json={})

        # Fill column 0 (6 moves)
        for _ in range(6):
            response = client.post('/api/make-move',
                                  json={'column': 0})
            if response.status_code != 200:
                break

        # Try one more move in full column
        response = client.post('/api/make-move',
                              json={'column': 0})
        assert response.status_code == 400

    def test_make_move_gravity(self, client):
        """Test that pieces drop to lowest row (gravity)."""
        # Start new game
        client.post('/api/new-game', json={})

        # First move in column 2
        response1 = client.post('/api/make-move',
                               json={'column': 2})
        data1 = response1.get_json()
        assert data1['move_row'] == 0  # Bottom row

        # Second move in same column
        response2 = client.post('/api/make-move',
                               json={'column': 2})
        data2 = response2.get_json()
        assert data2['move_row'] == 1  # One row up


class TestAIMoveAPI:
    """Tests for /api/ai-move endpoint."""

    def test_ai_move_basic(self, client):
        """Test AI making a move."""
        # Start new game
        client.post('/api/new-game', json={})

        # Human makes first move
        client.post('/api/make-move', json={'column': 3})

        # AI makes move
        response = client.post('/api/ai-move', json={})
        assert response.status_code == 200

        data = response.get_json()
        assert 'move' in data
        assert 'move_name' in data
        assert 'move_row' in data
        assert 'board' in data
        assert 'stats' in data

        # Check move is valid column
        assert 0 <= data['move'] < 7

        # Check move name is letter
        assert data['move_name'] in 'abcdefg'

        # Check stats present
        assert 'nodes_explored' in data['stats']
        assert 'max_tree_depth' in data['stats']
        assert 'simulations' in data['stats']

    def test_ai_move_with_thinking(self, client):
        """Test AI move with thinking stats (show_thinking=True)."""
        # Start new game
        client.post('/api/new-game', json={})

        # Human makes first move
        client.post('/api/make-move', json={'column': 3})

        # AI makes move with thinking stats
        response = client.post('/api/ai-move',
                              json={'show_thinking': True})
        assert response.status_code == 200

        data = response.get_json()
        assert 'evaluations' in data

        # Check evaluations format
        evals = data['evaluations']
        assert len(evals) > 0

        # Check first evaluation has required fields
        first_eval = list(evals.values())[0]
        assert 'value' in first_eval
        assert 'visits' in first_eval
        assert 'uct_score' in first_eval
        assert 'reasoning' in first_eval
        assert 'is_best' in first_eval

    def test_ai_move_statistics(self, client):
        """Test AI move statistics are sensible."""
        # Start new game with known simulations
        client.post('/api/new-game',
                   json={'num_simulations': 200})

        # AI makes first move
        response = client.post('/api/ai-move', json={})
        data = response.get_json()

        stats = data['stats']
        # Check nodes explored is reasonable
        assert stats['nodes_explored'] > 0
        assert stats['nodes_explored'] <= 1000  # Should be less than 5x simulations

        # Check tree depth is reasonable
        assert stats['max_tree_depth'] > 0
        assert stats['max_tree_depth'] < 42  # Can't be deeper than full board

        # Check simulations matches setting
        assert stats['simulations'] == 200


class TestUpdateSettingsAPI:
    """Tests for /api/update-settings endpoint."""

    def test_update_simulations(self, client):
        """Test updating MCTS simulation count."""
        response = client.post('/api/update-settings',
                              json={'num_simulations': 500})
        assert response.status_code == 200

        data = response.get_json()
        assert data['success'] is True
        assert data['num_simulations'] == 500

    def test_update_exploration_constant(self, client):
        """Test updating exploration constant."""
        response = client.post('/api/update-settings',
                              json={
                                  'num_simulations': 1000,
                                  'exploration_constant': 2.0
                              })
        assert response.status_code == 200

        data = response.get_json()
        assert data['exploration_constant'] == 2.0

    def test_update_max_depth(self, client):
        """Test updating max depth for depth-limited search."""
        response = client.post('/api/update-settings',
                              json={
                                  'num_simulations': 1000,
                                  'max_depth': 20
                              })
        assert response.status_code == 200

        data = response.get_json()
        assert data['max_depth'] == 20


class TestGameFlow:
    """Integration tests for complete game flow."""

    def test_complete_game_human_first(self, client):
        """Test complete game with human playing first."""
        # Start game
        response = client.post('/api/new-game', json={})
        assert response.status_code == 200

        # Play until game over (max 42 moves)
        for move_num in range(42):
            # Human move
            response = client.post('/api/make-move',
                                  json={'column': move_num % 7})
            if response.status_code != 200:
                break

            data = response.get_json()
            if data['is_terminal']:
                assert data['result'] in [-1.0, 0.0, 1.0]
                break

            # AI move
            response = client.post('/api/ai-move', json={})
            assert response.status_code == 200

            data = response.get_json()
            if data['is_terminal']:
                assert data['result'] in [-1.0, 0.0, 1.0]
                break

    def test_complete_game_ai_first(self, client):
        """Test complete game with AI playing first."""
        # Start game with AI first
        response = client.post('/api/new-game',
                              json={'ai_first': True})
        assert response.status_code == 200

        # AI already made first move
        data = response.get_json()
        assert sum(1 for x in data['board'] if x != 0) == 1

        # Continue game
        for move_num in range(41):  # One less since AI went first
            # Human move
            response = client.post('/api/make-move',
                                  json={'column': move_num % 7})
            if response.status_code != 200:
                break

            data = response.get_json()
            if data['is_terminal']:
                break

            # AI move
            response = client.post('/api/ai-move', json={})
            if response.status_code != 200:
                break

            data = response.get_json()
            if data['is_terminal']:
                break


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
