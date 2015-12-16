import minimax_search
import GameTree
import Heuristics
import sys

depth = 5

def human_vs_cpu(game):
	game_tree = GameTree.GameTree(depth, game.board, game.turn)

	# return the move the cpu player will make
	return minimax_search.run_minimax(game_tree.root, depth, -sys.maxint - 1, sys.maxint, Heuristics.maximize_threats)[1]

def cpu1(game):
	game_tree = GameTree.GameTree(depth, game.board, game.turn)

	# return the move the cpu player will make
	return minimax_search.run_minimax(game_tree.root, depth, -sys.maxint - 1, sys.maxint, Heuristics.streaks_234)[1]

def cpu2(game):
	game_tree = GameTree.GameTree(depth, game.board, game.turn)

	# return the move the cpu player will make
	return minimax_search.run_minimax(game_tree.root, depth, -sys.maxint - 1, sys.maxint, Heuristics.streaks_234)[1]
