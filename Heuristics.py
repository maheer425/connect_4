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

def beat_gabbi(board,turn):
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	if(checkForStreak(board,enemyColor,4)>0):
		return -1000000

def maximize_threats(board,turn):
	winningRowsP1 = 0
	score = 0
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	if(checkForStreak(board,enemyColor,4)>0):
		return -1000000

	for x in range(0,7):
		for y in range(0,6):
			winningColor = horizontal_winning_row(board,turn,x,y)
			if(turn == winningColor):
				score += 1
			elif(winningColor != "None"):
				score -= 1
			winningColor = vertical_winning_row(board,turn,x,y)
			if(turn == winningColor):
				score += 1
			elif(winningColor != "None"):
				score -= 1
			winningColor = urdiagonal_winning_row(board,turn,x,y)
			if(turn == winningColor):
				score += 1
			elif(winningColor != "None"):
				score -= 1
			winningColor = uldiagonal_winning_row(board,turn,x,y)
			if(turn == winningColor):
				score += 1
			elif(winningColor != "None"):
				score -= 1
	return score

def horizontal_winning_row(board,turn,x,y):
	found_color = False
	found_enemy_color = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	for i in range(x,x+4):
		if(i>=7):
			return "None"
		if(board[i][y] == turn):
			found_color = True
		if(board[i][y] == enemyColor):
			found_enemy_color = True
		if(found_color and found_enemy_color):
			return "None"
	if(found_color):
		return turn
	elif(found_enemy_color):
		return enemyColor
	else:
		return "None"

def vertical_winning_row(board,turn,x,y):
	found_color = False
	found_enemy_color = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	for i in range(y,y+4):
		if(i>=6):
			return "None"
		if(board[x][i] == turn):
			found_color = True
		if(board[x][i] == enemyColor):
			found_enemy_color = True
		if(found_color and found_enemy_color):
			return "None"
	if(found_color):
		return turn
	elif(found_enemy_color):
		return enemyColor
	else:
		return "None"

def urdiagonal_winning_row(board,turn,x,y):
	found_color = False
	found_enemy_color = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	j = y
	for i in range(x,x+4):
		if(i>=7 or j >=6):
			return "None"
		if(board[i][j] == turn):
			found_color = True
		if(board[i][j] == enemyColor):
			found_enemy_color = True
		if(found_color and found_enemy_color):
			return "None"
		j+=1
	if(found_color):
		return turn
	elif(found_enemy_color):
		return enemyColor
	else:
		return "None"

def uldiagonal_winning_row(board,turn,x,y):
	found_color = False
	found_enemy_color = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	j = y
	for i in range(x,x-4,-1):
		if(i<=0 or j >=6):
			return "None"
		if(board[i][j] == turn):
			found_color = True
		if(board[i][j] == enemyColor):
			found_enemy_color = True
		if(found_color and found_enemy_color):
			return "None"
		j+=1
	if(found_color):
		return turn
	elif(found_enemy_color):
		return enemyColor
	else:
		
		return "None"

def streaks_234(board, turn):
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
			if board[x][y].lower() == turn.lower():
				# check if a vertical streak starts at (i, j)
				count += verticalStreak(x, y, board, streak)
				
				# check if a horizontal four-in-a-row starts at (i, j)
				count += horizontalStreak(x, y, board, streak)
				
				# check if a diagonal (either way) four-in-a-row starts at (i, j)
				count += diagonalCheck(x, y, board, streak)
	# return the sum of streaks of length 'streak'
	return count
		
def verticalStreak(x, y, board, streak):
	consecutiveCount = 0
	for col in range(y, 6):
		if board[x][col].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break

	if consecutiveCount >= streak:
		return 1
	else:
		return 0

def horizontalStreak(x, y, board, streak):
	consecutiveCount = 0
	for row in range(x, 7):
		if board[row][y].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break

	if consecutiveCount >= streak:
		return 1
	else:
		return 0

def diagonalCheck(x, y, board, streak):

	total = 0
	# check for diagonals with positive slope
	consecutiveCount = 0
	row = x
	for col in range(y, 6):
		if row > 6:
			break
		elif board[row][col].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break
		row += 1 # incremented row when col is incremented
		
	if consecutiveCount >= streak:
		total += 1 

	# check for diagonals with negative slope
	consecutiveCount = 0
	row = x
	for col in range(y, -1, -1):
		if row > 6:
			break
		elif board[row][col].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break
		row += 1 # increment row when col is decremented

	if consecutiveCount >= streak:
		total += 1

	return total