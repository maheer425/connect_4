class Connect4:
	def __init__(self):
		self.turn = "red"
		self.board = [["empty" for y in range(6)] for x in range(7)]
		self.mode = -1 # 0, 1 or 2
		self.pieces = 0

	def checkWin(self,lastMove):
		x = lastMove[0]
		y = lastMove[1]
		for count in range(0,4):
			if(x-3+count >=0 and x+count <=6 and self.board[x-3+count][y] == self.turn and self.board[x-2+count][y] == self.turn and #check horizontal win
				self.board[x-1+count][y] == self.turn and self.board[x+count][y] == self.turn):
				print (self.turn + " won horizontal")
				return True
			elif(y-3+count >= 0 and y+count <=5 and self.board[x][y-3+count] == self.turn and self.board[x][y-2+count] == self.turn and #check vertical win
				self.board[x][y-1+count] == self.turn and self.board[x][y+count] == self.turn):
				print (self.turn + " won vertical")
				return True
			elif(x-3+count >= 0 and 3-y+count >= 0 and x+count <=6 and y+count <= 5 and self.board[x-3+count][y-3+count] == self.turn and self.board[x-2+count][y-2+count] == self.turn and #check diagonal win
				self.board[x-1+count][y-1+count] == self.turn and self.board[x+count][y+count] == self.turn):
				print (self.turn + " won diagonal")
				return True
			elif(x-count >= 0 and y-3+count >= 0 and x+3-count <=6 and y+count <= 5 and self.board[x+3-count][y-3+count] == self.turn and self.board[x+2-count][y-2+count] == self.turn and
				self.board[x+1-count][y-1+count] == self.turn and self.board[x-count][y+count] == self.turn):
				print (self.turn + " won diagonal 2")
				return True
		return False


	# the instance argument is the kivy widget button
	# gameLayout is the GUI for the game page
	def updateBoard(self, buttonNumber):
		nextPos = ()
		self.pieces += 1
		for y in range(0, 6):
			if(self.board[buttonNumber][y] == "empty"):
				nextPos = (buttonNumber, y)
				break
		if(nextPos != ()):
			self.board[nextPos[0]][nextPos[1]] = self.turn

			if(self.checkWin(nextPos)):
				self.endGame()
				return "game ended"
			if(self.pieces == 42):
				self.endGame()
			if(self.turn == "red"):
				self.turn = "yellow"
			else:
				self.turn = "red"

			return "game on"
			

	def endGame(self):
		pass
		#self.board =[["empty" for y in range(6)] for x in range(7)]