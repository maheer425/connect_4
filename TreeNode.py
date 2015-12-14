class TreeNode:
	def __init__(self):
		self.parent = None
		self.board = [["empty" for y in range(6)] for x in range(7)]
		self.turn = ""
		self.type = ""
		self.isLeaf = False
		self.children = []
		self.lastMove = -1
