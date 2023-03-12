import time

# --- Graphic Board ---
# prints the board in cosole with all the current values in lists r1-r6

def print_board():
    for i in range(6):
        index = 0
        tmp = ""
        for j in range(15):
            if j % 2 == 0:
                tmp += "|"
            else:
                tmp += board[i][index]
                index += 1
        print("    _ _ _ _ _ _ _ ")
        print(str(i+1) + "| " + tmp)

    print("    - - - - - - - \n    A B C D E F G ")

# --- Diagonal Check ---
# this function checks if there are any diagonal sets of 4 for input "X" or "O"

def diagonal_check(letter):
    for i in range(3):
        for j in range(4):
            if board[i][j] == letter and board[i+1][j+1] == letter and board[i+2][j+2] == letter and board[i+3][j+3] == letter:
                return True
    for i in range(3):
        for j in range(-1, -5, -1):
            if board[i][j] == letter and board[i+1][j-1] == letter and board[i+2][j-2] == letter and board[i+3][j-3] == letter:
                return True
    return False

# --- Horizontal Check ---
# this function checks if there are any horizontal sets of 4 for input "X" or "O"

def horizontal_check(letter):
    for i in range(6):
        for j in range(4):
            if board[i][j] == letter and board[i][j+1] == letter and board[i][j+2] == letter and board[i][j+3] == letter:
                return True
    return False

# --- Vertical Check ---
# this function checks if there are any vertical sets of 4 for input "X" or "O"

def vertical_check(letter):
    for i in range(3):
        for j in range(7):
            if board[i][j] == letter and board[i+1][j] == letter and board[i+2][j] == letter and board[i+3][j] == letter:
                return True
    return False

# --- Player Check ---
# this function checks if there are any diagonal, horizontal, or vertical sets of 4 for input "X" or "O"

def player_check(letter):
    return diagonal_check(letter) or horizontal_check(letter) or vertical_check(letter)

# --- Main Menu ---
# this function prints the mainmenu and takes inputs and opens new sections accordingly

def main_menu_input():
    print(
"""
░█▄█░█▀▀░█▀█░█░█
░█░█░█▀▀░█░█░█░█
░▀░▀░▀▀▀░▀░▀░▀▀▀

P - Play
S - Scores & Players
H - Help
C - Credits
E - Exit
"""
    )
    tmp = ""
    while tmp.upper() not in game_menu:
        tmp = input()

    tmp = tmp.upper()
    if tmp == "P":
        pass
    elif tmp == "S":
        print(
"""
░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█▀▀
░▀▀█░█░░░█░█░█▀▄░█▀▀░▀▀█
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀

"""
        )
        print(player_x_name + " (X): " + str(player_x_score))
        print(player_o_name + " (O): " + str(player_o_score))
        print("\n--------------------\n\n")
        print(
"""
░█▀█░█░░░█▀█░█░█░█▀▀░█▀▄░█▀▀
░█▀▀░█░░░█▀█░░█░░█▀▀░█▀▄░▀▀█
░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀

"""
        )
        print("Player X: " + player_x_name)
        print("Player O: " + player_o_name)
        print("\n--------------------\n\n")
        print("C - Change Names\nM - Main Menu")
        tmp2 = ""
        while tmp2.upper() != "C" and tmp2.upper() != "M":
            tmp2 = input()
        if tmp2.upper() == "C":
            get_names()
        else:
            main_menu_input()
    elif tmp == "H":
        print(
        """
░█░█░█▀▀░█░░░█▀█
░█▀█░█▀▀░█░░░█▀▀
░▀░▀░▀▀▀░▀▀▀░▀░░

A two-player connection game called "Connect Four"
has the players choose either "X" or "O" before taking
turns placing tokens into a seven-column, six-row rack.
The pieces land straight down, taking up the lowest
space in the column. Becoming the first player to
arrange four of their own tokens in a line that is
either horizontal, vertical, or diagonal is the game's
goal.

----------------------------

M - Main Menu
        """
        )
        back_input()
    elif tmp == "C":
        print(
"""
░█▀▀░█▀▄░█▀▀░█▀▄░▀█▀░▀█▀░█▀▀
░█░░░█▀▄░█▀▀░█░█░░█░░░█░░▀▀█
░▀▀▀░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀

Mohammadamin Moezzi
(portfolio project)
2023
Toronto, Canada

----------------------------

M - Main Menu
        """
        )
        back_input()
    else:
        print("GOODBYE!")
        exit()

# --- Back Input ---
# this function is for going back in certain menu's

def back_input():
    tmp = ""
    while tmp.upper() != "M":
        tmp = input()
    main_menu_input()

# --- Player Name Input ---
# This functions takes and saves the players' names in global variables

def get_names():
    global player_x_name
    global player_o_name
    player_x_name = input("What is the name for player X? ")
    player_o_name = input("What is the name for player O? ")
    print("Player X: " + player_x_name)
    print("Player O: " + player_o_name)
    time.sleep(3)
    main_menu_input()

# --- INITIAL VARIABLES ---
# 6 lists with 7 empty spots as in the original 6x7 board

r1 = [" ", " ", " ", " ", " ", " ", " "]
r2 = [" ", " ", " ", " ", " ", " ", " "]
r3 = [" ", " ", " ", " ", " ", " ", " "]
r4 = [" ", " ", " ", " ", " ", " ", " "]
r5 = [" ", " ", " ", " ", " ", " ", " "]
r6 = [" ", " ", " ", " ", " ", " ", " "]
board = [r1, r2, r3, r4, r5, r6]
letters = ["A", "B", "C", "D", "E", "F", "G"]
numbers = ["1", "2", "3", "4", "5", "6"]

player_x_score = 0
player_o_score = 0

game_menu = ["P", "S", "H", "C", "E"]

# --- Game Greeting ---
print(
"""
 _ _ _ _____ __    _____ _____ _____ _____ 
| | | |   __|  |  |     |     |     |   __|
| | | |   __|  |__|   --|  |  | | | |   __|
|_____|_____|_____|_____|_____|_|_|_|_____|
"""
)
print(
"""
 _____ _____ 
|_   _|     |
  | | |  |  |
  |_| |_____|
"""
)
print(
"""
 _____ _____ _____ _____ _____ _____ _____    ___ 
|     |     |   | |   | |   __|     |_   _|  | | |
|   --|  |  | | | | | | |   __|   --| | |    |_  |
|_____|_____|_|___|_|___|_____|_____| |_|      |_|
"""
)
print("___________________________________________\n\n")
time.sleep(3)
print("--- Please tell us your names ---")
get_names()
