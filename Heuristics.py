import random

def rando(board, turn):
	return random.randint(0,7)

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
	evenThreatsP1 = 0
	oddThreatsP1 = 0
	score = 0
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	if(checkForStreak(board,enemyColor,4)>0):
		return -1000000
	if(checkForStreak(board,turn,4)>0):
		return 10000000

	for x in range(0,7):
		for y in range(0,6):
			winningColor = horizontal_winning_row(board,turn,x,y)
			if(turn == winningColor):
				winningRowsP1 += 1
			elif(winningColor != "None"):
				winningRowsP1 -= 1
			winningColor = vertical_winning_row(board,turn,x,y)
			if(turn == winningColor):
				winningRowsP1 += 1
			elif(winningColor != "None"):
				winningRowsP1 -= 1
			winningColor = urdiagonal_winning_row(board,turn,x,y)
			if(turn == winningColor):
				winningRowsP1 += 1
			elif(winningColor != "None"):
				winningRowsP1 -= 1
			winningColor = uldiagonal_winning_row(board,turn,x,y)
			if(turn == winningColor):
				winningRowsP1 += 1
			elif(winningColor != "None"):
				winningRowsP1 -= 1
			winningColor = horizontal_threat(board,turn,x,y)
			if(turn == winningColor and x % 2 == 0):
				evenThreatsP1 +=1
			elif(turn == winningColor and x % 2 ==1):
				oddThreatsP1 +=1
			elif(winningColor == enemyColor and x%2 == 0):
				evenThreatsP1 -=1
			elif(winningColor == enemyColor and x%2 == 1):
				oddThreatsP1 -=1
			winningColor = urdiagonal_threat(board,turn,x,y)
			if(turn == winningColor and x % 2 == 0):
				oddThreatsP1 +=1
			elif(turn == winningColor and x % 2 ==1):
				evenThreatsP1 +=1
			elif(winningColor == enemyColor and x%2 == 0):
				oddThreatsP1 -=1
			elif(winningColor == enemyColor and x%2 == 1):
				evenThreatsP1 -=1
			winningColor = uldiagonal_threat(board,turn,x,y)
			if(turn == winningColor and x % 2 == 0):
				oddThreatsP1 +=1
			elif(turn == winningColor and x % 2 ==1):
				evenThreatsP1 +=1
			elif(winningColor == enemyColor and x%2 == 0):
				oddThreatsP1 -=1
			elif(winningColor == enemyColor and x%2 == 1):
				evenThreatsP1 -=1
	return .1*winningRowsP1 + evenThreatsP1 + oddThreatsP1

def horizontal_threat(board,turn,x,y):
	numFound = 0
	numEnemyFound = 0
	checkPos = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	for i in range(x,x+4):
		if(i>=7):
			return "None"
		if(board[i][y] == turn):
			numFound += 1
		if(board[i][y] == enemyColor):
			numEnemyFound += 1
		if(board[i][y] == "empty"):
			if(y>0 and board[i][y-1] == "empty"):
				checkPos = True
	if(numFound == 3 and checkPos):
		return turn
	elif(numEnemyFound == 3 and checkPos):
		return enemyColor
	else:
		return "None"

def urdiagonal_threat(board,turn,x,y):
	numFound = 0
	numEnemyFound = 0
	checkPos = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	j = y
	for i in range(x,x+4):
		if(i>=7):
			return "None"
		if(j >=6):
			return "None"
		if(board[i][j] == turn):
			numFound += 1
		if(board[i][j] == enemyColor):
			numEnemyFound += 1
		if(board[i][j] == "empty"):
			if(j>0 and board[i][j-1] == "empty"):
				checkPos = True
		j+=1
	if(numFound == 3 and checkPos):
		return turn
	elif(numEnemyFound == 3 and checkPos):
		return enemyColor
	else:
		return "None"

def uldiagonal_threat(board,turn,x,y):
	numFound = 0
	numEnemyFound = 0
	checkPos = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	j = y
	for i in range(x,x-4,-1):
		if(i<0):
			return "None"
		if(j >=6):
			return "None"
		if(board[i][j] == turn):
			numFound += 1
		if(board[i][j] == enemyColor):
			numEnemyFound += 1
		if(board[i][j] == "empty"):
			if(j>0 and board[i][j-1] == "empty"):
				checkPos = True
		j+=1
	if(numFound == 3 and checkPos):
		return turn
	elif(numEnemyFound == 3 and checkPos):
		return enemyColor
	else:
		return "None"

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
		#opp_threes = checkForStreak(board, opp_turn, 3)
		#opp_twos = checkForStreak(board, opp_turn, 2)
		if opp_fours > 0:
			return -100000
		else:
			return my_fours*100000 + my_threes*100 + my_twos*10
			

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
	for row in range(y, 6):
		if board[x][row].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break

	if consecutiveCount >= streak:
		return 1
	else:
		return 0

def horizontalStreak(x, y, board, streak):
	consecutiveCount = 0
	for column in range(x, 7):
		if board[column][y].lower() == board[x][y].lower():
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
	col = x
	for row in range(y, 6):
		if col > 6:
			break
		elif board[col][row].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break
		col += 1 # incremented row when col is incremented
		
	if consecutiveCount >= streak:
		total += 1 

	# check for diagonals with negative slope
	consecutiveCount = 0
	col = x
	for row in range(y, -1, -1):
		if col > 6:
			break
		elif board[col][row].lower() == board[x][y].lower():
			consecutiveCount += 1
		else:
			break
		col += 1 # increment row when col is decremented

	if consecutiveCount >= streak:
		total += 1

	return total