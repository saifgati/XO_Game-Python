# code by Gati SAif
# global variables
game_still_going = True

winner = False

current_player = "X"

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])

def handle_turn(player):
  print(player + "'s turn.")
  position = input("> Choose a position from 1 to 9: ")
  valid = False
  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("> Choose again.")

    position = int(position) - 1

    if board[position] == "-":
      valid =True
    else :
      print(" You can't go there, go again.")

  board[position] = player
  display_board()

def check_if_game_over():
  check_if_win()
  check_if_tie()
 

def check_if_win():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagnol_winner = check_diagnols()
  if row_winner :

      winner = row_winner

  elif column_winner:
    
      winner= column_winner

  elif diagnol_winner:
    
      winner = diagnol_winner 
  else :
    winner = False

  return

def check_rows():
  global game_still_going
  row_1 = board[0]== board[1]== board[2] !="-"
  row_2 = board[3]== board[4]== board[5] !="-"
  row_3 = board[6]== board[7]== board[8] !="-"
  if row_1 or row_2 or row_3:
    print(current_player + " won")
    game_still_going= False
  if row_1:
    board[0]
  elif row_2:
    board[1]
  elif row_3:
    board[2]
  return 

def check_columns():
  global game_still_going
  column_1 = board[0]== board[3]== board[6] !="-"
  column_2 = board[1]== board[4]== board[7] !="-"
  column_3 = board[2]== board[5]== board[8] !="-"
  if column_1 or column_2 or column_3:
    print(current_player + " won")

    game_still_going= False
  if column_1:
    board[0]
  elif column_2:
    board[3]
  elif column_3:
    board[6]
  return
def check_diagnols():
  global game_still_going
  diagnol_1 = board[0]== board[4]== board[8] !="-"
  diagnol_2 = board[6]== board[4]== board[2] !="-"
  
  if diagnol_1 or diagnol_2 :
    print(current_player + " won")

    game_still_going= False
  if diagnol_1:
    board[0]
  elif diagnol_2:
    board[6]
 
  return



def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    print("Tie.. play again !")
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

def play_game():
 #display initial board
  display_board()  
  while game_still_going:  
   handle_turn(current_player)
   check_if_game_over()
   flip_player()
  
print("Welcome !")
while 1:  
    y= input("(p) Play XO game (n) no thanx > ")
    while not ((y =="p") or (y== "n")) :
      y= input("Only valid characters are accepted  ----------------(p) Play XO game (n) no thanx > ")
      break
    if y=="n":
      print("Thank oyu for playing.")
      break
    elif y=="p":
      play_game()
    
