
def run_minimax (tree_node, d, minv, maxv, heuristic):
	'''Runs a minimax search on the given minimax tree node down to 
	a depth of d and returns the (score, move). move is in the range 
	0..6 '''
	if (d == 0 or tree_node.isLeaf == True):
		return (heuristic(tree_node.board, tree_node.turn), tree_node.lastMove)

	if (tree_node.type == "max"):
		node_value = minv
		move_to_make = -1 # initially we don't know which move to make
		for child_node in tree_node.children:
			(child_node_value, child_move) = run_minimax(child_node, d-1, node_value, maxv)
			if (child_node_value > node_value):
				node_value = child_node_value 
				move_to_make = child_node.lastMove
			if (node_value > maxv): # same as min <= max
				return (maxv, move_to_make)
		return (node_value, move_to_make)

	else: # type is min
		node_value = maxv
		move_to_make = -1 # initially we don't know which move to make
		for child_node in tree_node.children:
			(child_node_value, child_move) = run_minimax(child_node, d-1, minv, node_value)
			if (child_node_value < node_value):
				node_value = child_node_value
				move_to_make = child_node.lastMove
			if (node_value < minv):
				return (minv, move_to_make)
		return (node_value, move_to_make)