#!/usr/bin/env python
# coding: utf-8

# 

# In[13]:


def who_are_you():
    player1 = ''
    player2 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1.  Are you "X" or "O"?')
        if player1 == 'O':
            player2 = 'X'
        if player1 == 'X':
            player2 = 'O'
        else:
            print('Please choose "X" or "O"') 
        return {'p1': player1, 'p2': player2 }


# In[14]:


def ready_to_play():
    readycheck = 'wrong'
    
    while readycheck not in ['Y','N','y','n']:
        readycheck = input("Ready to play? (Y or N):")
        
        if readycheck not in ['Y','N','y','n']:
            print("sorry, please choose Y or N")
            
    if readycheck in['Y','y']:
        return True
    else:
        return False


# In[15]:


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# In[16]:


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


# In[17]:


# Returns True if game is over
# Returns False if no winner exists, and board still has empty spaces
# Returns 'tie' if no winner exists and board is full
def game_over(game_board):
    tie_test = ' '
    game_over = ''
    is_tie = False
    
    
#this is returning a game over because empty spaces equal eachother
    if (game_board[7] and game_board[8] and game_board[9] == 'X') or (game_board[4] and game_board[5] and game_board[6] == 'X') or (game_board[1] and game_board[2] and game_board[3] == 'X') or (game_board[1] and game_board[5] and game_board[9] == 'X') or (game_board[7] and game_board[5] and game_board[3] == 'X') or (game_board[1] and game_board[4] and game_board[7] == 'X') or (game_board[3] and game_board[6] and game_board[9] == 'X') or (game_board[2] and game_board[5] and game_board[8] == 'X') or (game_board[7] and game_board[8] and game_board[9] == 'O') or (game_board[4] and game_board[5] and game_board[6] == 'O') or (game_board[1] and game_board[2] and game_board[3] == 'O') or (game_board[1] and game_board[5] and game_board[9] == 'O') or (game_board[7] and game_board[5] and game_board[3] == 'O') or (game_board[1] and game_board[4] and game_board[7] == 'O') or (game_board[3] and game_board[6] and game_board[9] == 'O') or (game_board[2] and game_board[5] and game_board[8] == 'O'):
        game_over = True
        return game_over, is_tie
    if any(elem in tie_test for elem in game_board):
        game_over = False
    else:
        game_over = True
        is_tie = True
        
    return game_over, is_tie


# In[20]:


game_on = True
blank_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
end_of_game = False
is_tie = False
ready_check = ready_to_play()
player_dict = who_are_you() 
player1 = player_dict.get('p1')
player2 = player_dict.get('p2')

while game_on == True and end_of_game == False and ready_check == True and is_tie == False:
    game_board = place_choice(blank_board, player1)
    display_board(game_board)
    end_of_game = game_over(game_board)[0]
    is_tie = game_over(game_board)[1]
    
    #break out of loop if player 1 wins
    if end_of_game == True:
        continue
    game_board = place_choice(game_board, player2)
    display_board(game_board)
    end_of_game = game_over(game_board)[0]
    is_tie = game_over(game_board)[1]
else:
    game_on = False
    print("Game Over!")


# In[ ]:




