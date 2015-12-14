import minimax_search
import GameTree
import Heuristics
import sys

depth = 3

def human_vs_cpu(game):
	game_tree = GameTree.GameTree(depth, game.board, game.turn, Heuristics.baseline)

	# return the move the cpu player will make
	return minimax_search.run_minimax(game_tree.root, depth, -sys.maxint - 1, sys.maxint)[1]

def cpu_vs_cpu(self):
	pass