def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens_first(board, row, n):
    if row == n:
        return board[:]  # Return the first solution found

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            result = solve_n_queens_first(board, row + 1, n)
            if result:  # If solution found, return immediately
                return result
            board[row] = -1  # Backtrack
    return None  # No solution in this path

def print_solution(board, n):
    for row in range(n):
        line = ['Q' if i == board[row] else '.' for i in range(n)]
        print(" ".join(line))
    print()

def n_queens_one_solution(n):
    board = [-1] * n
    solution = solve_n_queens_first(board, 0, n)
    if solution:
        print("One valid n-Queens solution:")
        print_solution(solution, n)
    else:
        print("No solution exists.")

# Example: 8-Queens
n_queens_one_solution(8)
