class Go:

    BLACK = 'x'
    WHITE = 'o'

    def __init__(self, size):
        self.size = size
        self.board = [['.' for row in range(self.size)] for col in range(self.size)]
        self.player = BLACK

    def board(self):
        for row in self.board:
            for elem in self.board:
                print(elem + ' ', end='')
            
            print()

    def move(self, string):
        #! add checking
        row = int(string[0])
        col = string[1]
 
        row_coord = row - 1
        #! get rid of 'I'
        col_coord = col - 65

        
        self.board[row_coord][col_coord] = self.player
        nextPlayer()

    def nextPlayer():
        if self.player == BLACK:
            self.player = WHITE
        else:
            self.player = BLACK

