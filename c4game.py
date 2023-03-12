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
