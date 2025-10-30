# Function to try placing queens on the board
def placeQueens(i, cols, leftDiagonal, rightDiagonal, cur):
    n = len(cols)  # Get the size of the board

    # If all queens are placed, return True
    if i == n:
        return True

    # Try placing a queen in each column of the current row
    for j in range(n):
        # Skip if the column or diagonal is already occupied
        if cols[j] or rightDiagonal[i + j] or leftDiagonal[i - j + n - 1]:
            continue

        # Mark the column and diagonals as occupied
        cols[j] = 1 
        rightDiagonal[i + j] = 1
        leftDiagonal[i - j + n - 1] = 1
        
        # Add the current column to the solution path
        cur.append(j)

        # Recursively place queens on the next row
        if placeQueens(i + 1, cols, leftDiagonal, rightDiagonal, cur):
            return True  # If successful, return True

        # Backtrack: Remove the queen and reset the markings
        cur.pop()
        cols[j] = 0
        rightDiagonal[i + j] = 0
        leftDiagonal[i - j + n - 1] = 0

    # If no valid placement is found, return False
    return False

# Main function to solve the N-Queens problem
def nQueen(n):
    # Arrays to track column and diagonal occupations
    cols = [0] * n
    leftDiagonal = [0] * (n * 2)
    rightDiagonal = [0] * (n * 2)
    
    # List to store the positions of queens
    cur = []
    
    # Initialize the board with '.' to represent empty cells
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Try placing queens starting from the first row
    if placeQueens(0, cols, leftDiagonal, rightDiagonal, cur):
        # If successful, place queens on the board
        for i in range(n):
            board[i][cur[i]] = 'Q'
        return board
    else:
        # If no solution is found, return None
        return None

# Function to print the board
def printBoard(board):
    if board:
        # Print the board with queens placed
        for row in board:
            print(" ".join(row))
    else:
        # If no solution, notify the user
        print("No solution exists.")

# Input for number of queens
n = int(input("Enter the number of queens:\t"))

# Solve the N-Queens problem
board = nQueen(n)

# Print the result
printBoard(board)
