from sudoku import Sudoku

def main():
    n = int(input())
    sudoku = Sudoku(n)
    c = int(input())
    for _ in range(c):
        inputs = list(map(int, input().split()))
        i = inputs[0]
        j = inputs[1]
        value = inputs[2]
        sudoku.board[i][j] = value
    # sudoku.show()

if __name__ == '__main__':
    main()