
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

    def get_board_size(self):
        """
        Get the user input for the board size between 5 to 8 and validate the input value.
        """ 
        while True:  # Loop until valid input is provided
            try:
                size = int(input("Enter board size (5-8): "))
                if 5 <= size <= 8:  # Ensure size is within the valid range
                    return size
                else:
                    print("Please choose a size between 5 and 8.")
            except ValueError as e:
                print(f"Invalid data: {e}. Please enter a valid integer between 5 and 8.\n")

 
def main():
    """
    Run the Game
    """
    startbattle = BattleshipGame()
    print(startbattle.player_board.board)
    print(startbattle.computer_board.board)
 

print("Welcome to Battleship Game")
main()