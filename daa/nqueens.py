# Function to print the chessboard
def print_board(board, number_of_queens):
    for row in range(number_of_queens):
        for column in range(number_of_queens):
            print(board[row][column], end=" ")
        print()
    print("\n")  # Blank line for better readability


# Function to check if a queen can be placed safely at board[row][column]
def is_safe(board, row, column, number_of_queens):
    # Check the same column above
    for i in range(row):
        if board[i][column] == 1:
            return False

    # Check the upper left diagonal
    i = row - 1
    j = column - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper right diagonal
    i = row - 1
    j = column + 1
    while i >= 0 and j < number_of_queens:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Function to solve the N-Queens problem using backtracking
def solve_n_queens(board, current_row, number_of_queens):
    # Base case: If all queens are placed
    if current_row == number_of_queens:
        print_board(board, number_of_queens)
        return True

    # Try placing a queen in each column for the current row
    solution_found = False
    for column in range(number_of_queens):
        if is_safe(board, current_row, column, number_of_queens):
            board[current_row][column] = 1  # Place queen

            # Recur to place rest of the queens
            solution_found = solve_n_queens(board, current_row + 1, number_of_queens) or solution_found

            # Backtrack: remove the queen if it did not lead to a solution
            board[current_row][column] = 0

    return solution_found


# ---------------- Main Program ----------------
print("N-Queens Problem using Backtracking\n")

number_of_queens = int(input("Enter the number of queens: "))

# Create an empty NxN chessboard filled with 0
board = []
for i in range(number_of_queens):
    board.append([0] * number_of_queens)

# Place the first queen (for example at position [0][0])
board[0][0] = 1
print("\nThe first queen is placed at position (0, 0)\n")

# Solve for remaining queens
if not solve_n_queens(board, 1, number_of_queens):
    print("No solution exists for this configuration.")
