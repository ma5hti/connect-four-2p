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
        

# --- INITIAL VARIABLES ---
# 6 lists with 7 empty spots as in the original 6x7 board

r1 = [" ", " ", " ", " ", " ", " ", " "]
r2 = [" ", " ", " ", " ", " ", " ", " "]
r3 = [" ", " ", " ", " ", " ", " ", " "]
r4 = [" ", " ", " ", " ", " ", " ", " "]
r5 = [" ", " ", " ", " ", " ", " ", " "]
r6 = [" ", " ", " ", " ", " ", " ", " "]
board = [r1, r2, r3, r4, r5, r6]
