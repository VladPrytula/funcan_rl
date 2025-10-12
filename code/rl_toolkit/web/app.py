"""
Flask web application for interactive game-playing AI demos.

This file provides the base Flask app that all game projects reuse.
Individual game projects can import and extend this app.
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for local development

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    """Landing page listing available game demos."""
    games = [
        {
            'name': 'Tic-Tac-Toe',
            'url': '/tictactoe',
            'description': 'Exact DP solution (optimal play)',
            'week': 24
        },
        {
            'name': 'Connect Four',
            'url': '/connect-four',
            'description': 'MCTS + heuristics',
            'week': 31
        },
        {
            'name': 'Gomoku',
            'url': '/gomoku',
            'description': 'MCTS + neural network',
            'week': 40-41
        },
        {
            'name': 'Reversi',
            'url': '/reversi',
            'description': 'AlphaZero-Lite (self-play)',
            'week': '42-48'
        },
    ]
    return render_template('index.html', games=games)


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'})


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


# Main entry point
if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=5000)
