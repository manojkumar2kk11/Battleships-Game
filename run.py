
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

    def create_board(self, reveal_ships=False):
        """
        Method to create the board for players and computer, and to instruct reveal or not the ships based on the player or computer.
        Hide the computer's ships, show hits and misses only
        Show ships on the player's board or computer's revealed board
        """
        print("  " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            if self.computer and not reveal_ships:
                hidden_row = ["$" if cell == "S" else cell for cell in row]
                print(f"{idx} " + " ".join(hidden_row))
            else:
                print(f"{idx} " + " ".join(row)) 

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
     
    def show_boards(self):
        """
        Method to show both player's and computer's boards
        Player's ships are revealed
        Hide computer's ships
        """ 
        print("\nPlayer's Board (with ships):")
        self.player_board.create_board(reveal_ships=True)  
        print("\nComputer's Board (without ships):")
        self.computer_board.create_board(reveal_ships=False)  

 
def main():
    """
    Run the Game
    """
    startbattle = BattleshipGame()
    startbattle.show_boards()
 

print("Welcome to Battleship Game")
main()
