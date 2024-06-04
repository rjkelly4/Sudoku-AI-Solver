# Sudoku Solver

Sudoku solver is a pygame application allowing the player to play a game of sudoku that also visualizes a backtracking algorithm to 
show the player the solution and how it was solved.

## Features 

- Naive backtracking algorithm solves puzzle allowing player to see the steps taken to solve the puzzle 
- Highlights boxes once clicked
- In-game timer to keep track of how long it takes and make it more competitive
- 3 Life system, each error creates an X on the GUI
- Pencil-in feature: when you add a number to a square, it isn't set in stone right away allowing player to strategize
- Board randomizer on startup ensuring each game is a completely new puzzle ready to be solved

## Requirements

- pygame

## How to play

- Run 'python sudoku.py' in terminal
- Click on a square to select it
- Enter the number on the keyboard to pencil-in a number
- Once number is what the player wants to solidfy, hit the enter key
- Hit the space key to run the backtracking algorithm visualization at any point (also runs after game is over)
- Hit the delete key to clear a square
  
