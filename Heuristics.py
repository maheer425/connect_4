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

def maximize_threats(board,turn):
	winningRowsP1 = 0
	for x in range(0,7):
		for y in range(0,6):

def winning_row(board,turn):
	found_color = False
	found_enemy_color = False
	if(turn == "red"):
		enemyColor = "yellow"
	else:
		enemyColor = "red"
	for x in range(0,7):
		if(board[x,row] == turn):
			found_color = True
		if(board[x,row] == enemyColor):
			found_enemy_color = True
		if(found_color and found_enemy_color):
			return "None"
	if(found_color):
		return turn
	elif(found_enemy_color):
		return enemyColor
	else:
		return "None"