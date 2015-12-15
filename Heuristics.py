def baseline(board,turn):
	score = 0
	for x in range(0,7):
		for y in range(0,6):
			if(x>=1 and board[x-1][y] == turn and board[x][y] == turn):
				score += 1
			if(y>=1 and x>=1 and board[x-1][y-1] == turn and board[x][y] == turn):
				score += 1
			if(y>=1 and board[x][y-1] == turn and board[x][y] == turn):
				score +=1
			if(y>=1 and x<=5 and board[x+1][y-1] == turn and board[x][y] == turn):
				score +=1
			if(x<=5 and board[x+1][y] == turn and board[x][y] == turn):
				score +=1
			if(y<=4 and x<=5 and board[x+1][y+1] == turn and board[x][y] == turn):
				score +=1
			if(y<=4 and board[x][y+1] == turn and board[x][y] == turn):
				score +=1
			if(y<=4 and x>=1 and board[x-1][y+1] == turn and board[x][y] == turn):
				score +=1
	return score


def streaks_value(board, turn):
		""" Simple heuristic to evaluate board configurations
			Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 + 
			(num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
			3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
		"""
		opp_turn = ""
		if (turn == "yellow"):
			opp_turn = "red"
		else:
			opp_turn = "yellow"
		
		my_fours = checkForStreak(board, turn, 4)
		my_threes = checkForStreak(board, turn, 3)
		my_twos = checkForStreak(board, turn, 2)
		opp_fours = checkForStreak(board, opp_turn, 4)
		#opp_threes = self.checkForStreak(board, o_color, 3)
		#opp_twos = self.checkForStreak(board, o_color, 2)
		if opp_fours > 0:
			return -100000
		else:
			return my_fours*100000 + my_threes*100 + my_twos
			

def checkForStreak(board, turn, streak):
	count = 0
	# for each piece in the board...
	for y in range(6):
		for x in range(7):
			# ...that is of the color we're looking for...
			if board[x][y].lower() == color.lower():
				# check if a vertical streak starts at (i, j)
				count += verticalStreak(x, y, board, streak)
				
				# check if a horizontal four-in-a-row starts at (i, j)
				count += horizontalStreak(x, y, board, streak)
				
				# check if a diagonal (either way) four-in-a-row starts at (i, j)
				count += diagonalCheck(x, y, board, streak)
	# return the sum of streaks of length 'streak'
	return count
		
def verticalStreak(self, col, row, board, streak):
	consecutiveCount = 0
	for i in range(row, 6):
		if board[i][col].lower() == board[row][col].lower():
			consecutiveCount += 1
		else:
			break

	if consecutiveCount >= streak:
		return 1
	else:
		return 0

def horizontalStreak(col, row, board, streak):
	consecutiveCount = 0
	for j in range(col, 7):
		if board[row][j].lower() == board[row][col].lower():
			consecutiveCount += 1
		else:
			break

	if consecutiveCount >= streak:
		return 1
	else:
		return 0

def diagonalCheck(col, row, board, streak):

	total = 0
	# check for diagonals with positive slope
	consecutiveCount = 0
	j = col
	for i in range(row, 6):
		if j > 6:
			break
		elif board[i][j].lower() == board[row][col].lower():
			consecutiveCount += 1
		else:
			break
		j += 1 # increment column when row is incremented
		
	if consecutiveCount >= streak:
		total += 1

	# check for diagonals with negative slope
	consecutiveCount = 0
	j = col
	for i in range(row, -1, -1):
		if j > 6:
			break
		elif board[i][j].lower() == board[row][col].lower():
			consecutiveCount += 1
		else:
			break
		j += 1 # increment column when row is incremented

	if consecutiveCount >= streak:
		total += 1

	return total