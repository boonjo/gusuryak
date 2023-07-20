BOARD = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ]

def printBoard(board):
    """Prints the Sudoku Board

    Parameters
    ----------
    board : 2-D Array
        The matrix with the full information of the Sudoku Board

    Returns
    -------
    None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

def isEmpty(board):
    """Prints the Sudoku Board

    Parameters
    ----------
    board : 2-D Array
        The matrix with the full information of the Sudoku Board

    Returns
    -------
    None
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j  
    return None

def isValid(number, cell, board):
    """Checks to see if cell in the board is a valid number

    Parameters
    ----------
    number: int
        The number that will go into the selected cell to see if it's valid
    cell: tuple
        The cell in the board that is being checked
    board : 2-D Array
        The matrix with the full information of the Sudoku Board

    Returns
    -------
    True if valid, otherwise
    False
    """
    crow = cell[0]
    ccol = cell[1]
    
    for i in range(len(board)):
        if number == board[i][ccol]:
            return False
    for j in range(len(board[crow])):
        if number == board[crow][j]:
            return False

    # check the 3x3 grid
    row_mod = crow % 3
    col_mod = ccol % 3
    
    if row_mod == 0:
        row_rangel = crow
        row_rangeh = crow + 2
    elif row_mod == 1:
        row_rangel = crow - 1
        row_rangeh = crow + 1
    elif row_mod == 2:
        row_rangel = crow - 2
        row_rangeh = crow
        
    if col_mod == 0:
        col_rangel = ccol
        col_rangeh = ccol + 2
    elif col_mod == 1:
        col_rangel = ccol - 1
        col_rangeh = ccol + 1
    elif col_mod == 2:
        col_rangel = ccol - 2
        col_rangeh = ccol
    
    for i in range(row_rangel, row_rangeh+1):
        for j in range(col_rangel, col_rangeh+1):
            if number == board[i][j]:
                return False
    return True
    

# Approach to solving Sudoku
## Constraints:
### Each cell must contain a number ranging 1 - 9
### Each row must contain each number
### Each column must contain each number
### Each 3x3 block must contain each number
## Backtracking Algorithm
### Visit the empty cells
### Filll the digits sequentially
### Backtrack when the number filled is not valid

def solveBoard(board):
    """Solves the Sudoku Board

    Parameters
    ----------
    board : 2-D Array
        The matrix with the full information of the Sudoku Board

    Returns
    -------
    True if the board is solved
    False otherwise
    """
    # visit the empty cell
    backtrack_log = []
    empty_cell = isEmpty(board)
    if empty_cell is None:
        return True
    else:
        row, col = empty_cell
        for number in range(1, 10):
            if isValid(number, empty_cell, board):
                board[row][col] = number
                
                if solveBoard(board):
                    return True
                
                board[row][col] = 0
    return False
