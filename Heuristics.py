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
