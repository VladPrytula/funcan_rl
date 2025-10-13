"""
Game environments for reinforcement learning.

This module provides game environments that implement the BaseGameEnv interface,
enabling use with minimax solvers and other RL algorithms.

Available Environments:
- TicTacToe: Classic 3x3 Tic-Tac-Toe (generalized to nxn with k-in-a-row)
"""

from rl_toolkit.envs.base_game import BaseGameEnv
from rl_toolkit.envs.tictactoe import TicTacToe

__all__ = ['BaseGameEnv', 'TicTacToe']
