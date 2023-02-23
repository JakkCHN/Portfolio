from random import randint

#"def play_battleship():"  #this code here will allow me to put the whole game code into a method/funtion so that for reqierment 5 i can replay the game if the user says yes. However when i implement this line of code i cant get the whole programe to run, so i am unsure of the issue.
board = []

for x in range(6):
    board.append(["O"] * 6)                                                   # The code uses a 6x6 board filled with "O"s for the game of Battleship. Each row is a list of 6 "O"s, and the board is represented as a list of these rows.

def print_board(board):
    print("  1 2 3 4 5 6")                                                    # I have added numbers on the board 1-6 along with changing the board going from 0-5 
    row_num = 1
    for row in board:                                                         # Return a random number in the range 1-6 instead of 0-5.
        print(str(row_num) + " " + " ".join(row))
        row_num += 1

print("Let's play Battleship!")                                               # 1. On starting the game, ask if the user is playing in test-mode and accept an upper or lower case ‘y’ or ‘n’ as a valid answer
test_mode = input("Do you want to play in test mode? (y/n)").lower()          # Ask for test mode, the program prompts the user for input on whether they are playing in test-mode or not, and will only proceed if the user enters 'y' or 'n' (case-insensitive). If the user enters 'y', the program will print the location of the battleship. If they choose "n", the game will start as usual with the battleship hidden.                                                          
print_board(board)                                                            # lower() function to convert the user's input to lowercase so that we can check it against the lowercase letters "y" and "n"

if test_mode == "y":
    ship_row = randint(1, 6)                                                  # The print_board() function now takes in two additional parameters ship_row and ship_col that represent the location of the battleship.
    ship_col = randint(1, 6)
    print("The battleship is located in row: "), ship_row + 1                  
    print("                          column: "), ship_col + 1                 # +1 to both the ship_row and ship collum so that it matces with the changes made by reqirement 2
  
else:                                                                         # if the game is not being played in test mode, the print_board() function is called with the default values of -1 for ship_row and ship_col so that the function does not attempt to display the location of the battleship.
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)

def random_row(board):                                                        # Changes had to be made to be able to show location of ship for trial 
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)                                      # At the beginning of the game, a random location for the battleship is chosen using the random_row and random_col functions.

player_score = 0                                                              # Reqierment 6. To keep track of the score, i made two variables, one for the player's score and one for the computer's score, set to 0 before the game starts. Then, after each turn, checks if the battleships was sunk and add 1 point to the appropriate player.
computer_score = 0

for turn in range(9):
    print("Turn Number:"), turn                                               # 3. To change the code so that the user enters coordinates in the range 1 - 6 instead of 0 - 5, i modified the code  for the input statements for guess_row and guess_col to subtract 1 from the users input, and modifed the error-checking code accordingly to ensure the user enters a valid input in the new range
    guess_row = int(input("Guess Row (1-6):")) - 1                            # I have decided to - 1 to the users guess because i found the i had difficulty changing the actual place value of the O's.
    guess_col = int(input("Guess Col (1-6):")) - 1                            # This code subtracts 1 from the user input to match the index value for the board list
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk opponents battleship!")
        player_score += 1                                                     # if player wins +1 score to player
        break
    else: 
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed opponents4 battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 8:
            print("Game Over")
            computer_score += 1                                               # if player loses +1 score to computer

        print_board(board)
    turn += 1                                                                 # 2. The turn number must be displayed correctly.
print_board(board)                                                            # Changed from =+ 1, so that it increses by one instead

print("Final Score:")                                                         # final score displayed
print("Player Score: "), player_score
print("Computer Score: "), computer_score
print("Thanks for playing!")

play_again = input("Do you want to play again? (y/n)").lower()        
#  if play_again == "y":
#   play_battleship()                                                         # This code here corresponds to reqierment 6 i have attempted it but not been able to make it work with the rest of the code and so i have put it in #
#  else                                                                       # this replay section ask if the user wants to play again and if y then it will replay the code i have put into a method called "def play_battleship():"
#    print("Thanks for playing!")

#play_battleship()
    # ISSUES LIST
    # I am not able to add both of the guesses into a single input for reqierment 4
    #cant fully replay the game 
    