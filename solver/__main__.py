from solver import Sudoku
import time
from os import path

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
    default_file_name = 'sudoku.txt'
    file_name = default_file_name if (inp := input(f'Enter file name: (default: {default_file_name}) ')) == '' else inp
    BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
    with open(path.join(BASE_DIR, file_name)) as f:
        lines = f.readlines()
    n = int(lines[0])
    sudoku = Sudoku(n)
    c = int(lines[1])
    for line_num in range(2, c + 2):
        line = lines[line_num]
        inputs = list(map(int, line.split()))
        i = inputs[0]
        j = inputs[1]
        value = inputs[2]
        sudoku.set_entry(i, j, value)
    return sudoku

def main():
    inp = input('Read from file? [Y/n] ')
    sudoku = get_sudoku_from_commandline() if inp == 'n' else get_sudoku_from_file()
    print('Before solve:')
    sudoku.print_board()
    start_time = time.time()
    if sudoku.solve(0, 0):
        print('After solve:')
        sudoku.print_board()
    else:
        print('Unsolvable CSP!')
    print(f'Execution time: {time.time() - start_time} seconds')

if __name__ == '__main__':
    main()