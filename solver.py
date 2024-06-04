import pygame
import time
import random

def generate_board(level_difficulty): # level of difficulty -> easy = remove 40? medium = 50? hard = 60?
    grid = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(0, 9, 3):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for j in range(3):
            for k in range(3):
                grid[i+j][i+k] = numbers.pop()

    solve(grid)
    remove_cells(grid, level_difficulty)

    return grid

def remove_cells(grid, num_to_remove):
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for _ in range(num_to_remove):
        row, col = cells.pop()
        grid[row][col] = 0

def solve(board):
    """
    Recursively solves a sudoku board using backtracking

    Args:
        board (2D list of ints): the sudoku board we are trying to solve

    Returns:
        bool: true if the board was solved, false otherwise
    """
    find = find_empty(board)
    if not find: 
        return True # found the solution, we're done (board is completely filled)
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)): # checks to see if number i is valid in board
            board[row][col] = i # places i in the board at that valid index
            
            if solve(board): # recursively update the board until we eventually find solution or we loop through all nums and none are valid
                return True
            
            board[row][col] = 0 # if all options are exhausted, number can't be in right spot, in which case we reset
    
    return False

def valid(board, num, pos):
    """
    Checks to see if the attempted move is valid

    Args:
        board (2D list of ints): the sudoku board 
        num (int): the number we are putting into the board
        pos ((int, int)): the row, column of the board we are putting the number into

    Returns:
        bool: true if number is valid (no duplicates), false otherwise
    """
    # Checking row
    for i in range(len(board[0])): # would be 9, doing this way in case board gets bigger (?)
        if board[pos[0]][i] == num and pos[1] != i: # check each each element in the row and check if it equals num besides the row index we just put num in
            return False # 2 of the same number in one row

    # Checking col
    for i in range(len(board)): # loop through every row (0-9), doing this in case board gets bigger (?)
        if board[i][pos[1]] == num and pos[0] != i: # check each element in the col and check if it equals num besides the col index we just put num in
            return False # 2 of the same number in one col

    # Checking box
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y* 3 + 3): # loops through each box row
        for j in range(box_x * 3, box_x*3 + 3): # loops through each box col
            if board[i][j] == num and (i, j) != pos: # check each element in the m x n box and check if it equals num besides the (i, j) index we just put num in
                return False # 2 of the same number in one box
    
    return True # it is valid position, no duplicate

def find_empty(board):
    """
    Finds an empty space in the board

    Args:
        board (2D list of ints): the sudoku board

    Returns:
        tuple (int, int): row, col of the board
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col tuple
    return None

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

# print_board(board) # check board before algo
# solve(board) # run algo
# print("########################")
# print_board(board) # check board after algo

# print_board(generate_board(40))
# print("########################")
# print_board(generate_board(50))
# print("########################")
# print_board(generate_board(60))