
# Create a class Board 
class Board:
    def __init__(self, size, computer=False):
        """
        Initialise a new instance for the class board
        Size of board, computer, create default doller symbol for the size of the board.
        Ships and Guesses
        """
        self.size = size
        self.computer = computer
        self.board = [["$"] * size for _ in range(size)]
        self.ships = []
        self.guesses = set() 



