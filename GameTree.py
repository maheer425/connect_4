class GameTree:
	def __init__(self,depth,board,turn):
		self.root = TreeNode()
		self.root.board = board
		self.root.turn = turn
		self.root.type = "max"
		createTree(0,self.root,depth)
			

	def createTree(curdepth,parent,maxdepth):
		if(curdepth != maxdepth):
			for j in range(0,7):
				if checkLegal(parent.board,j):
					child = TreeNode()
					child.parent = parent
					child.lastMove = j
					if(parent.turn == "red"):
						child.turn = "yellow"
					else:
						child.turn = "red"
					if(parent.type == "max"):
						child.type = "min"
					else:
						child.type = "max"
					child.board = parent.board
					updateBoard(child,j)
					parent.children.append(child)
					createTree(curdepth+1,child,maxdepth)

	def checkLegal(board,move):
		nextPos = ()
		for y in range(0, 6):
			if(board[move][y] == "empty"):
				return True
		return False

	def updateBoard(node,move):
		nextPos = ()
		for y in range(0, 6):
			if(node.board[move][y] == "empty"):
				nextPos = (move, y)
		node.board[nextPos[0]][nextPos[1]] = node.turn