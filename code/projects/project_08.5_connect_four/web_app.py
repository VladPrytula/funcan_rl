"""
Flask web application for Connect Four with MCTS AI.

Usage:
    python web_app.py
    Visit http://localhost:5002/connect-four

Theory Connection (Syllabus Week 27-28):
    - MCTS with UCT ([THM-28.X.Y])
    - Connect Four as finite MDP ([THM-24.X.Y])
"""

from flask import Flask, render_template, jsonify, request
import sys
import os

# Add rl_toolkit to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from rl_toolkit.envs.connect_four import ConnectFour
from rl_toolkit.algorithms.mcts import MCTSSolver

app = Flask(__name__, template_folder='../../rl_toolkit/web/templates')

# Game state storage (in-memory, single player for now)
game_state = {
    'env': ConnectFour(),
    'solver': MCTSSolver(num_simulations=1000)
}


@app.route('/connect-four')
def connect_four():
    """Serve Connect Four web interface."""
    return render_template('connect_four.html')


@app.route('/api/new-game', methods=['POST'])
def new_game():
    """
    Start new game with configurable settings.

    Request JSON:
        {
            'rows': int (default: 6),
            'cols': int (default: 7),
            'num_simulations': int (default: 1000),
            'ai_first': bool (default: False)
        }

    Returns:
        {
            'board': list[int],
            'current_player': int (1 or -1),
            'legal_moves': list[int],
            'rows': int,
            'cols': int
        }
    """
    data = request.json or {}
    rows = data.get('rows', 6)
    cols = data.get('cols', 7)
    num_simulations = data.get('num_simulations', 1000)
    ai_first = data.get('ai_first', False)

    # Create new game
    game_state['env'] = ConnectFour(rows=rows, cols=cols)
    game_state['solver'] = MCTSSolver(num_simulations=num_simulations)

    env = game_state['env']

    # If AI plays first, make AI move
    if ai_first:
        solver = game_state['solver']
        move = solver.search(env, maximize=(env.current_player == 1))
        env.step(move)

    return jsonify({
        'board': env.board.tolist(),
        'current_player': int(env.current_player),
        'legal_moves': env.get_legal_moves().tolist(),
        'rows': env.rows,
        'cols': env.cols,
        'ai_first': ai_first
    })


@app.route('/api/make-move', methods=['POST'])
def make_move():
    """
    Human makes move in specified column.

    Request JSON:
        {
            'column': int (0 to cols-1)
        }

    Returns:
        {
            'board': list[int],
            'current_player': int,
            'legal_moves': list[int],
            'is_terminal': bool,
            'result': float or None,
            'move_row': int  # Row where piece landed
        }
    """
    data = request.json
    col = data['column']

    env = game_state['env']

    # Validate move
    if col not in env.get_legal_moves():
        return jsonify({'error': 'Illegal move'}), 400

    # Find row where piece will land (for animation)
    row = env._find_lowest_row(col)

    # Make move
    env.step(col)

    return jsonify({
        'board': env.board.tolist(),
        'current_player': int(env.current_player),
        'legal_moves': env.get_legal_moves().tolist(),
        'is_terminal': env.is_terminal(),
        'result': float(env.get_result(player=1)) if env.is_terminal() else None,
        'move_row': row
    })


@app.route('/api/ai-move', methods=['POST'])
def ai_move():
    """
    AI makes move using MCTS.

    Request JSON:
        {
            'show_thinking': bool (default: False)
        }

    Returns:
        {
            'move': int (column index),
            'move_name': str (column letter),
            'move_row': int (row where piece landed),
            'board': list[int],
            'current_player': int,
            'legal_moves': list[int],
            'is_terminal': bool,
            'result': float or None,
            'stats': dict (nodes_explored, max_tree_depth, simulations),
            'evaluations': dict (optional, if show_thinking=True)
        }
    """
    data = request.json or {}
    show_thinking = data.get('show_thinking', False)

    env = game_state['env']
    solver = game_state['solver']

    # Get MCTS statistics for visualization (if requested)
    evaluations = None
    if show_thinking:
        evaluations = solver.get_candidate_evaluations(env, maximize=(env.current_player == 1))
    else:
        # Just run MCTS search
        move = solver.search(env, maximize=(env.current_player == 1))

    # If evaluations were computed, extract best move from there
    if evaluations:
        move = max(evaluations.items(), key=lambda x: x[1]['visits'])[0]

    # Find row where piece will land (for animation)
    row = env._find_lowest_row(move)

    # Make move
    env.step(move)

    response = {
        'move': int(move),
        'move_name': chr(ord('a') + move),
        'move_row': row,
        'board': env.board.tolist(),
        'current_player': int(env.current_player),
        'legal_moves': env.get_legal_moves().tolist(),
        'is_terminal': env.is_terminal(),
        'result': float(env.get_result(player=1)) if env.is_terminal() else None,
        'stats': solver.get_stats()
    }

    # Include evaluations if requested
    if evaluations:
        # Convert all values to JSON-serializable types
        response['evaluations'] = {
            str(k): {
                'value': float(v['value']),
                'visits': int(v['visits']),
                'uct_score': float(v['uct_score']),
                'reasoning': str(v['reasoning']),
                'is_best': bool(v['is_best'])
            } for k, v in evaluations.items()
        }

    return jsonify(response)


@app.route('/api/update-settings', methods=['POST'])
def update_settings():
    """
    Update MCTS settings without starting new game.

    Request JSON:
        {
            'num_simulations': int,
            'exploration_constant': float (optional),
            'max_depth': int or None (optional)
        }

    Returns:
        {
            'success': bool,
            'num_simulations': int,
            'exploration_constant': float,
            'max_depth': int or None
        }
    """
    data = request.json
    num_simulations = data.get('num_simulations', 1000)
    exploration_constant = data.get('exploration_constant', 1.41)
    max_depth = data.get('max_depth', None)

    # Create new solver with updated settings
    game_state['solver'] = MCTSSolver(
        num_simulations=num_simulations,
        c=exploration_constant,
        max_depth=max_depth
    )

    return jsonify({
        'success': True,
        'num_simulations': num_simulations,
        'exploration_constant': exploration_constant,
        'max_depth': max_depth
    })


if __name__ == '__main__':
    print("=" * 70)
    print("Connect Four Web Interface")
    print("=" * 70)
    print("Starting server...")
    print("Visit: http://localhost:5002/connect-four")
    print()
    print("Theory Connection (Syllabus Week 27-28):")
    print("  [THM-28.X.Y]: MCTS with UCT achieves logarithmic regret per node")
    print("  UCT formula: Q(s,a) + c√(ln N(s) / N(s,a))")
    print("=" * 70)

    app.run(port=5002, debug=True)
