
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

# Create a class battleship Game
class BattleshipGame:
    def __init__(self):
        """
        Initialise a new instance for the class battleship Game
        Get the size of board from user,create board for player and computer, Number of ships in the board based on the board size.
        Hits, attempts and maximum number of attempts can be multiple by the size of the board
        """
        self.size = self.get_board_size()
        self.player_board = Board(self.size)  
        self.computer_board = Board(self.size, computer=True)  
        self.num_ships = self.size 
        self.hits = 0
        self.attempts= 0
        self.max_attempts = self.size * 2  
