from math import sqrt

class Sudoku:
    def __init__(self, n: int):
        self.size = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.possible_numbers = [[set(i + 1 for i in range(self.size)) for i in range(self.size)] for j in range(self.size)]
    
    def set_entry(self, i: int, j: int, value: int) -> None:
        self.board[i][j] = value
    
    def move_to_next_cell(self, i: int, j: int) -> tuple:
        j += 1
        if j >= self.size:
            j %= self.size
            i += 1
        return i, j
    
    def is_empty(self, i: int, j: int) -> bool:
        return self.board[i][j] == 0

    def has_conflict(self, i: int, j: int, p: int, q: int) -> bool:
        if self.is_empty(i, j) or self.is_empty(p, q) or (i == p and j == q): # cannot check for conflicts!
            return False
        return self.board[i][j] == self.board[p][q]
    
    def is_valid(self, i: int, j: int) -> bool:
        # row-wise check
        for c in range(self.size):
            if c == j:
                continue
            elif self.has_conflict(i, c, i, j):
                return False

        # column-wise check
        for r in range(self.size):
            if r == i:
                continue
            elif self.has_conflict(r, j, i, j):
                return False
        
        # box-wise check
        r = int((i // sqrt(self.size)) * sqrt(self.size)) # initial box row
        c = int((j // sqrt(self.size)) * sqrt(self.size)) # initial box column

        for r_count in range(int(sqrt(self.size))):
            for c_count in range(int(sqrt(self.size))):
                if self.has_conflict(r + r_count, c + c_count, i, j):
                    return False
        
        return True
    
    def solve(self, i: int, j: int) -> bool:
        if i >= self.size or j >= self.size:
            return True
        while not self.is_empty(i, j):
            i, j = self.move_to_next_cell(i, j)
        for value in self.possible_numbers[i][j]:
            self.set_entry(i, j, value)
            if self.is_valid(i, j):
                p, q = self.move_to_next_cell(i, j)
                if self.solve(p, q):
                    return True
        return False

    def print_board(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(f'{str(self.board[i][j]).rjust(len(str(self.size)), "0")} ', end='')
            print('')

if __name__ == '__main__':
    # checking the class
    sud = Sudoku(25)
    sud.set_entry(24, 3, 21)
    sud.print_board()