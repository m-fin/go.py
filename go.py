class Go:

    def __init__(self, size):
        self.size = size
        self.board = [['.' for row in range(self.size)] for col in range(self.size)]

        self.players = {
            'BLACK' : 'x',
            'WHITE' : 'o'
        }

        self.player = self.players['BLACK']

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem + ' ', end='')
            
            print()

    def move(self, string):
        #! add checking
        row = int(string[0])
        col = string[1]
 
        y_coord = row - 1
        #! get rid of 'I'
        x_coord = ord(col) - 65
     
        self.board[self.size - y_coord - 1][x_coord] = self.player
        self.nextPlayer()

    def nextPlayer(self):
        if self.player == self.players['BLACK']:
            self.player = self.players['WHITE']
        else:
            self.player = self.players['BLACK']
