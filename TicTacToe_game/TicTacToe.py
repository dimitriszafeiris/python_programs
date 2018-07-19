from IPython.display import clear_output
import random

#Display main board
def display_board(board):
    clear_output()  
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Player choice of X or O
def player_input():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()

	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')

# Place marker at board
def place_marker(board, marker, position):
    board[position] = marker

# Check if player played last has won
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# First to play
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Check for space box
def space_check(board, position):
    return board[position] == ' '

# Check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Decide next position
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))   
    return position

# Ask for rematch
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Start logic of the game
print ('Welcome to our game.')
while True:

	#Setting up the game
	the_board = [' ']*10
	player1_marker,player2_marker = player_input()
	turn = choose_first()
	print (turn + ' will play first.')

	play_game = input('Ready to play? y or n? ')
	if play_game == 'y':
		game_on = True
	else:
		game_on = False

	#GAME
	while game_on:
		if turn == 'Player 1':
			#show board 
			display_board(the_board)

			#Choose a position
			position = player_choice(the_board)

			#Place the marker at selected position
			place_marker(the_board,player1_marker,position)

			if win_check(the_board,player1_marker):
				display_board(the_board)
				print('Player 1 has won!')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board(the_board)
					print ('The game is tie.')
					game_on = False
				else:
					turn = 'Player 2'
		else:
			#show board 
			display_board(the_board)

			#Choose a position
			position = player_choice(the_board)

			#Place the marker at selected position
			place_marker(the_board,player2_marker,position)

			if win_check(the_board,player2_marker):
				display_board(the_board)
				print('Player 2 has won!')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board(the_board)
					print ('The game is tie.')
					game_on = False
				else:
					turn = 'Player 1'

	if not replay():
		break
