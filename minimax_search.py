
def run_minimax (tree_node, minv, maxv, heuristic):
	'''Runs a minimax search on the given minimax tree node down to 
	a depth of d and returns the (score, move). move is in the range 
	0..6 '''
	if (tree_node.isLeaf == True):
		return (heuristic(tree_node.board, tree_node.turn), tree_node.lastMove)

	if (tree_node.type == "max"):
		updated_minv = minv # this will change as we get child values

		move_to_make = -1 # initially we don't know which move to make
		for child_node in tree_node.children:
			(child_node_value, child_move) = run_minimax(child_node, updated_minv, maxv, heuristic)
			if (child_node_value > updated_minv):
				updated_minv = child_node_value
				move_to_make = child_node.lastMove

			if (maxv <= updated_minv): 
				return (updated_minv, move_to_make)
		return (updated_minv, move_to_make)

	else: # type is min
		updated_maxv = maxv # this will change as we get child values

		move_to_make = -1 # initially we don't know which move to make
		for child_node in tree_node.children:
			(child_node_value, child_move) = run_minimax(child_node, minv, updated_maxv, heuristic)
			if (child_node_value < updated_maxv):
				updated_maxv = child_node_value
				move_to_make = child_node.lastMove

			if (updated_maxv <= minv):
				return (updated_maxv, move_to_make)
		return (updated_maxv, move_to_make)