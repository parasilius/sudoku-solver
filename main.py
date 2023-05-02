from sudoku import Sudoku
import time

def get_sudoku_from_commandline():
    n = int(input())
    sudoku = Sudoku(n)
    c = int(input())
    for _ in range(c):
        inputs = list(map(int, input().split()))
        i = inputs[0]
        j = inputs[1]
        value = inputs[2]
        sudoku.set_entry(i, j, value)
    return sudoku

def get_sudoku_from_file():
    with open('sudoku.txt') as f:
        lines = f.readlines()
    n = int(lines[0])
    sudoku = Sudoku(n)
    c = int(lines[1])
    for line_num in range(2, c):
        line = lines[line_num]
        inputs = list(map(int, line.split()))
        i = inputs[0]
        j = inputs[1]
        value = inputs[2]
        sudoku.set_entry(i, j, value)
    return sudoku

def main():
    sudoku = get_sudoku_from_file()
    start_time = time.time()
    if sudoku.solve(0, 0):
        sudoku.print_board()
    else:
        print('Unsolvable CSP!')
    print(f'Execution time: {time.time() - start_time} seconds')

if __name__ == '__main__':
    main()