"""
The project consists of programming a valid chess board with a white king, a white queen, and the black king.
The program runs the black king's turn, and it will return all of the possible moves that are available to the
Black King, according to the specific movements of the white queen and king. The program will check if
there is a check, and if there are no possible moves determine of there is a checkmate. 
"""
import random

def switchStamp(s):
    if s == "@":
        s = "#"
    else:
        s = "@"
    return s

def makeBoard():
    board =[]
    stamp = "@"
    for r in range(8):
        row = []
        for c in range(8):
            row.append(stamp)
            stamp = switchStamp(stamp)
        board.append(row)
        stamp = switchStamp(stamp)
    return board

def printBoard(board):
    for r in range(8):
        for c in range(8):
            print(b[r][c], end=" ")
        print()

#Place white king, randomly: K
#Place black king, randomly: k
#Place white king, randomly: Q
#Return modified board
def setBoard(board):
    rowK = random.randrange(0,8)
    colK = random.randrange(0,8)
    board[rowK][colK] = "K"

    rowk = random.randrange(0,8)
    colk = random.randrange(0,8)
    diffR = abs(rowK - rowk)
    diffC = abs(colK - colk)

    while diffR < 2 and diffC < 2:
        rowk = random.randrange(0,8)
        colk = random.randrange(0,8)
        diffR = abs(rowK - rowk)
        diffC = abs(colK - colk)
    board[rowk][colk] = "k"

    rowQ = random.randrange(0,8)
    colQ = random.randrange(0,8)
    while board[rowQ][colQ] == "K" or board[rowQ][colQ] == "k":
        rowQ = random.randrange(0,8)
        colQ = random.randrange(0,8)
    board[rowQ][colQ] = "Q"
    return board

b = []
#Depending of the introduced number, the program will work with a radom board (1) or a predefined one (2)
choice = int(input())
if choice == 1:
    b = makeBoard()
    b = setBoard(b)
elif choice == 2:
    for r in range(8):
        line = input()
        line = line.strip()
        row = line.split(" ")
        b.append(row)
printBoard(b)

"""
With the use of the entire board(array) and the required character, this function
iterates through all the lines and rows within the [0] and [1] parameters and when it 
matches the required position, it matches i and j to a new empty list n..
"""
#It returns an n list with the values of the position of given character
def position_piece(array, character):
    n = [0,0]
    for i in range(8):
        for j in range(8):
            if array[i][j] == character:
                n[0] = i
                n[1] = j
                return n
#The function helps detemine if the given values of a position do not over pass the limitations of the board.
#If it is within ranges the fucntion returns true. 
def inBounds(pos):
    if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
        return True
    else:
        return False
#This function helps determine if the values in a given set of positions is within the ranges 
#The function returns True if the positions are not in range. 
def isAnyOutofBounce(positions):
    for p in positions:
        if inBounds(p) == False:
            return True
    return False

#All of the surrounding positions of a given piece will be calculated through the sum and rest of specific positions in a determined range.
#This fucntion returns all of the positions (8)

def possible_moves(board, position):
    positionbk = position
    r = positionbk[0]
    c = positionbk[1]
    positionsbk = [[r, c+1], [r-1, c+1], [r-1, c], [r-1, c-1], [r, c-1], [r+1, c-1], [r+1, c], [r+1, c+1]]
    while isAnyOutofBounce(positionsbk):
        for pos in positionsbk:
            if inBounds(pos) == False:
                positionsbk.remove(pos)
    return positionsbk

#This function will limit the kind of stamps that can be pulled in the movements of the queen, excluding the White King (K)
#If the stamps are not equal to the white king positions, it returns True, and if the stamps == the white king, it equals False

def stamps(array,row,column):
    stamp = array[row][column]
    if stamp == 'K':
        return False
    elif stamp == '@' or stamp == '#' or stamp == 'k':
        return True

#This function will take the position of the queen, and from that position go all the positions up and down, in the given range of the board.
#The stamps function is included so that the integration of positions stop when it encounters a white king (K)
def queen_vertical_view(array):
    queen = position_piece(b, 'Q')
    vertical = []
    x = queen[0]
    y = queen[1]
    for i in range(x-1,-1,-1):
        if stamps(array, i, y):
            vertical.append([i, y])
        else:
            break   
    for e in range(x+1,8,1):
        if stamps(array, e, y):
            vertical.append([e , y])
        else:
            break     
    return vertical  

#This function will take the position of the queen and through addition and substraction go to all the positions on the right and the left in the given range of the board.
#The stamps function is included so that the integration of positions stop when it encounters a white king (K)

def queen_horizontal_view(array):
    queen = position_piece(b, 'Q')
    horizontal = []
    x = queen[0]
    y = queen[1] 
    for i in range(y+1,8,1):
        if stamps(array, x, i):
            horizontal.append([x, i])
        else:
            break   
    for j in range(y-1,-1,-1):
        if stamps(array, x, j):
            horizontal.append([x, j])
        else:
            break
    return horizontal

#As from the others, with the position of the queen and with the addition and substraction of the position, the down diagonal will be calculated.
#The stamps function is included so that the integration of positions stop when it encounters a white king (K)

def queen_slash1(array):
    queen = position_piece(b, 'Q')
    slash1 = []
    x = queen[0]
    y = queen[1] 
    x1 = x
    y1 = y
    for i in range(0,7,1):
        x1 += 1
        y1 += 1
        if x1 < 8 and y1 < 8:
            if stamps(array,x1,y1):
                slash1.append([x1, y1])
        else:
            break
    x2 = x
    y2 = y
    for i in range(0,7,1):
        x2 -= 1
        y2 -= 1
        if x2 > -1 and y2 > -1:
            if stamps(array,x2,y2):
                slash1.append([x2, y2])
        else:
            break
    return slash1

#As from the others, with the position of the queen and with the addition and substraction of the position, the up diagonal will be calculated.
#The stamps function is included so that the integration of positions stop when it encounters a white king (K)

def queen_slash2(array):
    queen = position_piece(b, 'Q')
    slash2 = []
    x = queen[0]
    y = queen[1] 
    x1 = x
    y1 = y
    for i in range(0,7,1):
        x1 -= 1
        y1 += 1
        if x1 > -1 and y1 < 8:
            if stamps(array,x1,y1):
                slash2.append([x1, y1])
        else:
            break
    x2 = x
    y2 = y
    for i in range(0,7,1):
        x2 += 1
        y2 -= 1
        if y2 > -1 and x2 < 8:
            if stamps(array,x2,y2):
                slash2.append([x2, y2])
        else:
            break
    return slash2

#Given all the possible positions of the queen, the white king and the black king, if a position of the black king is in the list of the positions of the queen or white king, those positions will be removed.
#The new set of positions will be returned

def real_moves(moves):
    possible_wk_moves = possible_moves(b, position_piece(b,'K'))
    queen_vertical_moves = queen_vertical_view(b)
    queen_horizontal_moves = queen_horizontal_view(b)
    queen_slash_down = queen_slash1(b)
    queen_slash_up = queen_slash2(b)
    for i in moves[:]:
        if i in possible_wk_moves:
            moves.remove(i)
        elif i in queen_vertical_moves:
            moves.remove(i)
        elif i in queen_horizontal_moves:
            moves.remove(i)
        elif i in queen_slash_down:
            moves.remove(i)
        elif i in queen_slash_up:
            moves.remove(i)
    return moves

#If any of the black king positions matches a position in the white queen list, it will return true, meaning there is a check.
#If a black king position is within a queen position, the function returns True, else it returns false.

def check_check():
    positionBK = position_piece(b,'k')
    queen_vertical_moves = queen_vertical_view(b)
    queen_horizontal_moves = queen_horizontal_view(b)
    queen_slash_down = queen_slash1(b)
    queen_slash_up = queen_slash2(b)

    if positionBK in queen_vertical_moves:
        return True
    elif positionBK in queen_horizontal_moves:
        return True
    elif positionBK in queen_slash_down:
        return True
    elif positionBK in queen_slash_up:
        return True
    else:
        return False
#In the end, if the possible moves of the black king is empty, the function will return True, meaning there is indeed a checkmate.
def check_mate(real_moves):
    if not real_moves:
        return True
    else:
        return False


check = check_check()
checkMate = check_mate(real_moves(possible_moves(b, position_piece(b,'k'))))
print("Black King Moves:", real_moves(possible_moves(b, position_piece(b,'k'))))
print("Check:", check)
print("Checkmate:", checkMate)

