import minimax_search
import GameTree
import Heuristics
import connect4
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


if __name__ == "__main__":
	draws = 0
	red_wins = 0
	red_losses = 0

	num_games_to_play = 20

	connect4_game = connect4.Connect4()
	first_turns = True 
	while (num_games_to_play > 0): 

		print "cpu1 thinking"
		if (first_turns): # introduce random variation 
			cpu1_move_num = Heuristics.rando()
		else:	
			cpu1_move_num = cpu1(connect4_game)
		

		status = connect4_game.updateBoard(cpu1_move_num)
		if (status == "red won"):
			red_wins += 1
			num_games_to_play -= 1
			first_turns = True
			connect4_game = connect4.Connect4()
			continue 

		if (status == "yellow won"):
			red_losses += 1
			num_games_to_play -= 1
			first_turns = True
			connect4_game = connect4.Connect4()
			continue

		if (status == "draw"):
			draws += 1
			num_games_to_play -= 1
			first_turns = True
			connect4_game = connect4.Connect4()
			continue

		print "cpu2 thinking"
		if (first_turns): # introduce random variation 
			cpu2_move_num = Heuristics.rando()
			first_turns = False
		else:	
			cpu2_move_num = cpu1(connect4_game)

		status = connect4_game.updateBoard(cpu2_move_num)

		if (status == "red won"):
			red_wins += 1
			num_games_to_play -= 1
			first_turns = True
			connect4_game = connect4.Connect4()
			continue 

		if (status == "yellow won"):
			red_losses += 1
			num_games_to_play -= 1
			first_turns = True
			connect4_game = connect4.Connect4()
			continue

		if (status == "draw"):
			draws += 1
			num_games_to_play -= 1
			first_turns = True
			connect4_game = connect4.Connect4()
			continue

	print ("draws: " + str(draws))
	print ("red wins: " + str(red_wins))
	print ("red losses: " + str(red_losses))
	while(True):
		continue