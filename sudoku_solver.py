board = [
    [3,6,4,0,9,0,0,0,0],
    [0,5,0,1,0,6,0,2,7],
    [0,2,7,0,0,5,0,4,6],
    [0,7,3,6,0,1,0,0,4],
    [4,0,2,3,0,0,1,0,0],
    [6,0,0,2,0,0,0,8,0],
    [8,3,0,9,6,0,4,0,0],
    [0,0,0,0,2,8,5,0,0],
    [0,0,0,0,1,0,6,7,8]
]

#function to display board
def display_board(b):    
    for i in range(len(b)):
        print("")
        if i%3 == 0 and i!= 0:
            print("- - - - - - - - - - - -")
        for j in range(len(b[0])):
            if j%3 == 0 and j!= 0:
                print(" | ", end="")
            print(str(b[i][j]) + " ", end="")

#function to find empty square
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)

    return False

#checking if input is valid
def check(b, inp, pos):

    #checking the row
    for i in range(len(b[0])):
        if b[pos[0]][i] == inp and pos[1] != i:
            return False
        
    #checking the column    
    for i in range(len(b)):    
        if b[i][pos[1]] == inp and pos[0] != i:
            return False
        
    #checking the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(3):
        for j in range(3):
            if b[box_y * 3 + i][box_x * 3 + j] == inp and pos[0] != box_y * 3 + i and pos[1] != box_x * 3 + j:
                return False      
    return True

def solve(b):
    empty = find_empty(board)
    if empty == False:
        return True
    
    for i in range(1, 10):
        if check(board, i, empty):
            b[empty[0]][empty[1]] = i

            if solve(board):
                return True

            b[empty[0]][empty[1]] = 0

print("Initial board")
display_board(board)

solve(board)

print("\n\nSolved board")
display_board(board)
