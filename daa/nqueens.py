def is_safe(board, row, col):
    n = len(board)
    for r in range(n):
        if r == row:
            continue
        c = board[r]
        if c == -1:
            continue
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_from_row(board, start=0):
    n = len(board)
    # find next empty row
    row = start
    while row < n and board[row] != -1:
        row += 1
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_from_row(board, row + 1):
                return True
            board[row] = -1
    return False

def print_board(board):
    n = len(board)
    for r in range(n):
        print(" ".join('Q' if board[r] == c else '.' for c in range(n)))
    print()

def n_queens_with_first(n, first_row=-1, first_col=-1):
    board = [-1] * n
    if first_row != -1 and first_col != -1:
        if not (0 <= first_row < n and 0 <= first_col < n):
            print("First queen coordinates out of range.")
            return
        board[first_row] = first_col
        if not is_safe(board, first_row, first_col):
            print("Pre-placed queen conflicts with another (invalid).")
            return

    if solve_from_row(board, 0):
        print(f"One valid {n}-Queens solution (respecting pre-placed queen):")
        print_board(board)
    else:
        print("No solution exists for the given pre-placement.")

if __name__ == "__main__":
    n = int(input("Enter board size n (e.g., 8): "))
    fr = int(input("Enter row of first queen (0-indexed) or -1 to skip: "))
    fc = -1
    if fr != -1:
        fc = int(input("Enter column of first queen (0-indexed): "))
    n_queens_with_first(n, first_row=fr, first_col=fc)
