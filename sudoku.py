class Sudoku:
    def __init__(self, n: int):
        self.size = n
        self.board = [[0 for i in range(n)] for j in range(n)]
    
    def add_entry(self, i: int, j: int, value: int):
        self.board[i][j] = value
    
    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                print(f'{str(self.board[i][j]).rjust(len(str(self.size)), "0")} ', end='')
            print('')

if __name__ == '__main__':
    # checking the class
    sud = Sudoku(25)
    sud.add_entry(24, 3, 21)
    sud.show()