import TreeNode
import copy
import Heuristics

def checkLegal(board,move):
	for y in range(0, 6):
		if(board[move][y] == "empty"):
			if(Heuristics.checkForStreak(board,"red",4) < 1 and Heuristics.checkForStreak(board,"yellow",4) < 1):
				return True
	return False

def updateBoard(node, move):
	nextPos = ()
	for y in range(0, 6):
		if(node.board[move][y] == "empty"):
			nextPos = (move, y)
			break
	node.board[nextPos[0]][nextPos[1]] = node.turn

class GameTree:
	def __init__(self,depth,board,turn):
		self.root = TreeNode.TreeNode()
		self.root.board = copy.deepcopy(board)
		self.root.turn = turn
		self.root.type = "max"
		self.createTree(0, self.root, depth)
			


	def createTree(self, curdepth,parent,maxdepth):
		if(curdepth != maxdepth):
			for j in range(0,7):
				if checkLegal(parent.board,j):
					child = TreeNode.TreeNode()
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
					child.board = copy.deepcopy(parent.board)
					updateBoard(child,j)
					if(curdepth == maxdepth-1):
						child.isLeaf = True
					parent.children.append(child)
					self.createTree(curdepth+1, child, maxdepth)
