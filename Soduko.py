# Define the Sudoku grid (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Function to find an empty cell 
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col  # Return position of the empty cell
    return None

# Function to check if a number can be placed in a given cell
def is_valid(grid, num, pos):
    row, col = pos

    # Check the row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Backtracking function to solve the puzzle
def solve(grid):
    empty = find_empty(grid)
    if not empty:  
        return True
    row, col = empty

    for num in range(1, 10): 
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num 

            # Recursively attempt to fill in the rest of the puzzle
            if solve(grid):
                return True

            # If unsuccessful, reset and backtrack
            grid[row][col] = 0

    return False  # Trigger backtracking

print("Unsolved Sudoku Grid:")
print_grid(sudoku_grid)
if solve(sudoku_grid):
    print("\nSolved Sudoku Grid:")
    print_grid(sudoku_grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
