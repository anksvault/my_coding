#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Sharma                                              #
# Script      : ticTacToe.py                                              #
# Py Versions : 3.5                                                       #
# Required    : IPython.display                                           #
# Execute     : python ticTacToe.py                                       #
#=========================================================================#

from IPython.display import clear_output

def display_board(board):
  print('The Tic-Tac-Toe Board will look like the following.')
  print(' '+board[0]+' | '+board[1]+' | '+board[2])
  print('---|---|---')
  print(' '+board[3]+' | '+board[4]+' | '+board[5])
  print('---|---|---')
  print(' '+board[6]+' | '+board[7]+' | '+board[8])
  
  print('\nRules:\n1. Users will have to select the position of the matrix when their turn comes.')
  print('2. Any user placing his/her symbol in a straight or diagonal lines first, wins!')
  print('3. If none of the users are able to win till the end, this will result in a draw!')
  print('4. Any Incorrect move beyond 0-9 or overwriting existing move will result in Penalty resulting in your move getting cancelled and would be give to next player instead.')
  print('Ex: Player #1 Turn: 2. This will give the following: ')
  print('   |   | X')
  print('---|---|---')
  print('   |   |  ')
  print('---|---|---')
  print('   |   |  ')

def symbol_selection():
  while True:
    P1=str(input('Player #1: Please select your symbol (X or O): ')).upper()
    if P1 == 'X':
      print('Player #1 Symbol: {}'.format('X'))
      print('Player #2 Symbol: {}'.format('O'))
      return 'X'
    elif P1 == 'O':
      print('Player #1 Symbol: {}'.format('O'))
      print('Player #2 Symbol: {}'.format('X'))
      return 'O'
    else:
      print('Please enter your choice between the following symbols only (X/O)')

def gameplay(P1,P2):
  print('--------------------------------- GAME START ---------------------------------')
  uv=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
  
  ctr=0
  
  while ctr < 9:
    if (uv[0]==uv[1]==uv[2]==P1) or (uv[3]==uv[4]==uv[5]==P1) or (uv[6]==uv[7]==uv[8]==P1) or (uv[0]==uv[3]==uv[6]==P1) or (uv[1]==uv[4]==uv[7]==P1) or (uv[2]==uv[5]==uv[8]==P1) or (uv[0]==uv[4]==uv[8]==P1) or (uv[2]==uv[4]==uv[6]==P1):
      return 'Player 1 Wins!!!'
    elif (uv[0]==uv[1]==uv[2]==P2) or (uv[3]==uv[4]==uv[5]==P2) or (uv[6]==uv[7]==uv[8]==P2) or (uv[0]==uv[3]==uv[6]==P2) or (uv[1]==uv[4]==uv[7]==P2) or (uv[2]==uv[5]==uv[8]==P2) or (uv[0]==uv[4]==uv[8]==P2) or (uv[2]==uv[4]==uv[6]==P2):
      return 'Player 2 Wins!!!'
    elif ctr%2==0:
      POI=int(input('Player #1 Turn: '))
      
      if (POI >= 0 and POI  <=8) and (uv[POI] != 'X' and uv[POI] != 'O'):
        uv[POI]=P1
        
        # Print the current Board Status
        print(' '+uv[0]+' | '+uv[1]+' | '+uv[2])
        print('---|---|---')
        print(' '+uv[3]+' | '+uv[4]+' | '+uv[5])
        print('---|---|---')
        print(' '+uv[6]+' | '+uv[7]+' | '+uv[8])
      
        # Increment in counter
        ctr+=1

    elif ctr%2!=0:
      PTI=int(input('Player #2 Turn: '))
      
      if (PTI >= 0 and PTI  <=8) and (uv[PTI] != 'X' and uv[PTI] != 'O'):
        uv[PTI]=P2
        
        # Print the current Board Status
        print(' '+uv[0]+' | '+uv[1]+' | '+uv[2])
        print('---|---|---')
        print(' '+uv[3]+' | '+uv[4]+' | '+uv[5])
        print('---|---|---')
        print(' '+uv[6]+' | '+uv[7]+' | '+uv[8])
      
      else:
        print('Penalty: Invalid Selection! You lose this move.')
      
      ctr+=1
    
  return 'DRAW!!!'


# Function Calls
display_board(['X','O','X','O','X','O','X','O','X']) ## Test Board
P1=symbol_selection()  ## Players' Symbol Selection
if P1 == 'X':
  print('Result: {}'.format(gameplay('X','O'))) # The actual gameplay function and loops.
else:
  print('Result: {}'.format(gameplay('O','X'))) # The actual gameplay function and loops.
