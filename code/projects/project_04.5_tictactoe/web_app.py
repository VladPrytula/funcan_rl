#!/usr/bin/env python3
"""
Web application for Tic-Tac-Toe with optimal AI.

Serves the game in a browser with real-time AI moves via API.

Usage:
    python web_app.py                    # Default port 5001
    python web_app.py --port 8080        # Custom port
    python web_app.py --host 0.0.0.0     # Expose to network

"""

import sys
import os
import time
import argparse

# Add rl_toolkit to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from flask import Flask, render_template, jsonify, request
from rl_toolkit.envs.tictactoe import TicTacToe
from rl_toolkit.algorithms.minimax import MinimaxSolver

# Create Flask app
app = Flask(__name__,
            template_folder='../../rl_toolkit/web/templates',
            static_folder='../../rl_toolkit/web/static')


@app.route('/')
def index():
    """Redirect to game."""
    return render_template('tictactoe.html')


@app.route('/tictactoe')
def tictactoe():
    """Serve Tic-Tac-Toe game."""
    return render_template('tictactoe.html')


@app.route('/tictactoe/move', methods=['POST'])
def get_ai_move():
    """
    API endpoint for AI move computation.

    Request JSON:
    {
        "board": [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Flattened board state
        "board_size": 3,  # Optional, default 3
        "win_length": 3   # Optional, default board_size
    }

    Response JSON:
    {
        "move": 4,  # Move index
        "stats": {
            "nodes_explored": 4941,
            "cache_hits": 2209,
            "cache_size": 2732,
            "heuristic_evals": 0,
            "compute_time_ms": 123.45
        }
    }
    """
    try:
        data = request.get_json()
        board_flat = data['board']
        board_size = data.get('board_size', 3)
        win_length = data.get('win_length', board_size)

        # Reconstruct game state
        env = TicTacToe(board_size=board_size, win_length=win_length)
        env.board = [[board_flat[i*board_size + j] for j in range(board_size)] for i in range(board_size)]
        import numpy as np
        env.board = np.array(env.board, dtype=np.int8)
        env.current_player = -1  # AI is always player -1 (O)

        # Check if game is already over
        if env.is_terminal():
            return jsonify({'error': 'Game is already over'}), 400

        # Configure search depth based on board size
        if board_size == 3:
            max_depth = None  # Exact search
        elif board_size == 4:
            max_depth = 8
        elif board_size >= 5:
            max_depth = 4
        else:
            max_depth = None

        # Compute optimal move
        solver = MinimaxSolver(max_depth=max_depth)
        start_time = time.time()
        move = solver.get_best_move(env, maximize=False)  # AI minimizes (player -1)
        compute_time = time.time() - start_time

        # Get stats
        stats = solver.get_stats()
        stats['compute_time_ms'] = round(compute_time * 1000, 2)

        return jsonify({
            'move': int(move),
            'stats': stats
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/tictactoe/candidates', methods=['POST'])
def get_candidate_evaluations():
    """
    API endpoint for candidate move evaluations.

    This endpoint evaluates all legal moves and returns their minimax values,
    useful for visualization and understanding why the AI chooses particular moves.

    Request JSON:
    {
        "board": [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Flattened board state
        "board_size": 3,  # Optional, default 3
        "win_length": 3   # Optional, default board_size
    }

    Response JSON:
    {
        "candidates": {
            "0": {
                "value": 0.10,
                "reasoning": "Balanced position",
                "depth_used": null,  # null for exact search, int for depth-limited
                "is_best": false,
                "is_terminal": false
            },
            "4": {
                "value": 0.00,
                "reasoning": "Balanced position",
                "depth_used": null,
                "is_best": true,
                "is_terminal": false
            },
            ...
        },
        "best_move": 4,
        "stats": {
            "nodes_explored": 5477,
            "cache_hits": 2891,
            "cache_size": 2586,
            "heuristic_evals": 0,
            "compute_time_ms": 450.23
        }
    }

    Notes:
    -----
    This endpoint is more computationally expensive than /tictactoe/move because
    it evaluates all legal moves independently. However, the shared memoization
    cache helps reduce redundant computation.

    Expected compute times:
    - 3×3: ~200-300ms (evaluates 9 moves)
    - 4×4: ~10-15s (evaluates 16 moves, depth-limited)
    - 5×5: ~8-12s (evaluates 25 moves, depth-limited)

    The frontend should show a loading indicator and potentially disable the
    toggle when computation is in progress.

    Theory Connection (Week 24):
    This endpoint exposes V*(s,a) for all actions a, demonstrating the Bellman
    optimality equation: π*(s) = argmax_a Q*(s,a) = argmax_a V*(s,a)
    """
    try:
        data = request.get_json()
        board_flat = data['board']
        board_size = data.get('board_size', 3)
        win_length = data.get('win_length', board_size)

        # Reconstruct game state
        env = TicTacToe(board_size=board_size, win_length=win_length)
        env.board = [[board_flat[i*board_size + j] for j in range(board_size)] for i in range(board_size)]
        import numpy as np
        env.board = np.array(env.board, dtype=np.int8)
        env.current_player = -1  # AI is always player -1 (O)

        # Check if game is already over
        if env.is_terminal():
            return jsonify({'error': 'Game is already over'}), 400

        # Configure search depth based on board size
        if board_size == 3:
            max_depth = None  # Exact search
        elif board_size == 4:
            max_depth = 8
        elif board_size >= 5:
            max_depth = 4
        else:
            max_depth = None

        # Evaluate all candidate moves
        solver = MinimaxSolver(max_depth=max_depth)
        start_time = time.time()
        evaluations = solver.get_candidate_evaluations(env, maximize=False)  # AI minimizes (player -1)
        compute_time = time.time() - start_time

        # Get stats
        stats = solver.get_stats()
        stats['compute_time_ms'] = round(compute_time * 1000, 2)

        # Find best move
        best_move = None
        for move_idx, data in evaluations.items():
            if data['is_best']:
                best_move = move_idx
                break

        # Convert keys to strings for JSON (JavaScript requires string keys)
        candidates_json = {str(k): v for k, v in evaluations.items()}

        return jsonify({
            'candidates': candidates_json,
            'best_move': int(best_move) if best_move is not None else None,
            'stats': stats
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok', 'game': 'tictactoe'})


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Tic-Tac-Toe Web Server')
    parser.add_argument('--port', type=int, default=5001,
                        help='Port to run the server on (default: 5001, avoids macOS AirPlay on 5000)')
    parser.add_argument('--host', type=str, default='127.0.0.1',
                        help='Host to bind to (default: 127.0.0.1, use 0.0.0.0 to expose to network)')
    parser.add_argument('--no-debug', action='store_true',
                        help='Disable debug mode')
    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("  TIC-TAC-TOE WEB SERVER")
    print("=" * 60)
    print(f"\n🌐 Starting server at http://{args.host}:{args.port}")
    print("\n📱 Open your browser and navigate to:")
    print(f"   http://localhost:{args.port}/tictactoe")
    if args.host == '0.0.0.0':
        print(f"   Or from another device: http://YOUR_IP:{args.port}/tictactoe")
    print("\n⚡ Features:")
    print("   - Click squares to make moves")
    print("   - AI responds with optimal play")
    print("   - View search statistics (nodes explored, cache hits)")
    print("   - Switch who goes first")
    print("\n💡 Tips:")
    print(f"   - Default port {args.port} (avoids macOS AirPlay on 5000)")
    print("   - Use --port 8080 to change port")
    print("   - Use --host 0.0.0.0 to expose to network")
    print("\n" + "=" * 60)
    print("Press Ctrl+C to stop the server")
    print("=" * 60 + "\n")

    try:
        app.run(debug=not args.no_debug, host=args.host, port=args.port)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ ERROR: Port {args.port} is already in use!")
            print(f"\n💡 Try a different port:")
            print(f"   python web_app.py --port {args.port + 1}")
            print("\n🍎 On macOS, port 5000 is used by AirPlay Receiver.")
            print("   Solution: Use port 5001 (default) or disable AirPlay in System Settings")
            sys.exit(1)
        else:
            raise
