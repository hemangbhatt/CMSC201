# File:       proj1.py
# Author:     Hemang Bhatt
# Date:       11/15/15
# Section:    30
# E-mail:     hb6@umbc.edu
# Description:
# This file contains code of a simple cellular automata game,called Conway's Game of Life.
# In this game user have a grid where pixels can either on or off (alive or dead). In the game,
# as time marches on, there are simple rules that govern wheather each pixel will be on or off.

ALIVE = "A"
DEAD  = "."

# This function takes in the current board as a parameter and prints out the board's contents.
def printBoard(board):
    print()
    for row in range(len(board)):
        for column in range(len(board[row])):
            print(board[row][column], end = "")
        print()

# This function takes the current board in as a parameter, and that returns a new board with next
# iteration. 
def nextIteration(board):
    
    # copy nextBoard from board
    nextBoard = []
    for i in board:
        nextBoard.append(list(i))
        
    row_min = 0
    column_min = 0
    row_max = len(board)
    column_max = len(board[0])
    # These loops will go through each cell in board, and if conditons will count live neighbors.
    for row in range(row_max):
        for column in range(column_max):
            # Counter will count live neighbors.
            counter = 0
            # Check above cell
            if ((row - 1) >= row_min):
                if board[(row - 1)][column] == ALIVE: 
                    counter += 1
            # Check left side cell
            if ((column - 1) >= column_min):
                if board[row][(column - 1)] == ALIVE: 
                    counter += 1
            # Check below cell
            if ((row + 1) < row_max):
                if board[(row + 1)][column] == ALIVE: 
                    counter += 1
            # Check right side cell
            if ((column + 1) < column_max):
                if board[row][(column + 1)] == ALIVE: 
                    counter += 1
            # Check upper left corner cell
            if (((row - 1) >= row_min) and ((column - 1) >= column_min)) :
                if board[(row - 1)][(column - 1)] == ALIVE: 
                    counter += 1
            # Check upper right corner cell
            if (((row - 1) >= row_min) and ((column + 1) < column_max)):
                if board[(row - 1)][(column + 1)] == ALIVE: 
                    counter += 1
            # Check lower left corner cell
            if (((row + 1) < row_max) and ((column - 1) >= column_min)):
                if board[(row + 1)][(column - 1)] == ALIVE: 
                    counter += 1
            # Check lower right corner cell
            if (((row + 1) < row_max) and ((column + 1) < column_max)):
                if board[(row + 1)][(column + 1)] == ALIVE: 
                    counter += 1

            # The game rules are as follows:
            # Any live cell with fewer than two live neighbors dies.
            # Any live cell with two or three live neighbors lives on to the next generation.
            # Any live cell with more than three live neighbors dies.
            # Any dead cell with exactly three live neighbors becomes a live cell.

            if counter < 2: nextBoard[row][column] = DEAD
            if counter == 3: nextBoard[row][column] = ALIVE
            if counter > 3: nextBoard[row][column] = DEAD
    return nextBoard


def main():
    
    # Get input value of rows greater than or equal to 1
    rows = int(input("Please enter number of rows: "))
    while rows < 1:
        if rows < 1: print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")
        rows = int(input("Please enter number of rows: "))

    # Get input value of columns greater than or equal to 1
    columns = int(input("Please enter number of columns: "))
    while columns < 1:
        if columns < 1: print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")
        columns = int(input("Please enter number of columns: "))

    board = []
    nextBoard = []
    # These loops create empty board
    for row in range (rows):
        board.append([])
        for column in range (columns):
            board[row].append(DEAD)

    row = ""
    QUIT = 'q'
    # turn on cells of board
    while row != QUIT:
        print()
        row = input("Please enter the row of a cell to turn on (or q to exit): ")
        if ((row != QUIT) and (int(row) not in range(rows))):
            print("\tThat is not valid value; please enter a number\n\t between 0 and ", int(rows)-1, "inclusive...\n")
        elif row != QUIT:
            column = int(input("Please enter a column for that cell: "))
            while (column not in range(columns)):
                print("\tThat is not valid value; please enter a number\n\t between 0 and ", int(columns)-1, "inclusive...\n")
                column = int(input("Please enter a column for that cell: "))
            board[int(row)][int(column)] = ALIVE

    numIteration = int(input("How many iteration should I run? "))
    while numIteration < 0:
        print("\nThat is not a valid value; please enter a number\n\t greater than or equal to 0")
        numIteration = int(input("How many iteration should I run? "))

    print("Starting Board:")
    printScreen = printBoard(board)

    # print iteration
    for i in range(numIteration):
        print("\nIteration", i+1, ":")
        nextBoard   = nextIteration(board) # Assign 2D list to nextBoard
        board = [] 
        # Copy List from nextBoard to board
        for k in nextBoard:
            board.append(list(k))
        # print board
        printScreen = printBoard(board)
main()
