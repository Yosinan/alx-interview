import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    
        # Check diagonals
        if abs(i - row) == abs(board[i] - col):
            return False
    
    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = []
    board = [-1] * N
    
    def solve(row):
        if row == N:
            solutions.append([(i, board[i]) for i in range(N)])
            return
        
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(row + 1)
                board[row] = -1
    
    solve(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solutions = solve_nqueens(N)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
