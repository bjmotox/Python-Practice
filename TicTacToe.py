def who_are_you():
    player1=''
    player2=''
    
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1.  Are you "X" or "O"?')
        if player1 == 'O':
            player2 = 'X'
        if player1 == 'X':
            player2 = 'O'
        else:
            print('Please choose "X" or "O"')
            
        
    return player1,player2


def ready_to_play():
    readycheck = 'wrong'
    
    while readycheck not in ['Y','N','y','n']:
        readycheck = input("Keep Playing? (Y or N):")
        
        if readycheck not in ['Y','N','y','n']:
            print("sorry, please choose Y or N")
            
    if readycheck == 'Y' or 'y':
        return True
    else:
        return False


def display_board(board):
    # this will take a list (the current board status), and print the results
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def place_choice(game_board, player):
    new_board = game_board
    choice = '22'
    players_turn = player
    
    
    while choice not in (1,2,3,4,5,6,7,8,9):
        choice = int(input("Pick a position\n7 8 9\n4 5 6\n1 2 3:"))
        if choice not in [1,2,3,4,5,6,7,8,9]:
            print("sorry, invalid choice")
    if players_turn == 'X':
        new_board[choice] = 'X'
    else:
        new_board[choice] = 'O'
    
    return new_board


# this needs to be rebuilt
def game_over(game_board):
    function_complete = False
    tie_test = ' '
    game_over = ''
    
    while function_complete == False:
        if game_board[7] == game_board[8] == game_board[9] or game_board[4] == game_board[5] == game_board[6] or game_board[1] == game_board[2] == game_board[3] or game_board[1] == game_board[5] == game_board[9] or game_board[7] == game_board[5] == game_board[3] or game_board[1] == game_board[4] == game_board[7] or game_board[3] == game_board[6] == game_board[9] or game_board[2] == game_board[5] == game_board[8]:
            function_complete = True
            game_over = True
        if any(elem in tie_test for elem in game_board):
            function_complete = True
            game_over = False
        else: 
            pass
            
    return game_over


