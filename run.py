# Import the random number module
import random

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
                hidden_row = ["$" if cell == "@" else cell for cell in row]
                print(f"{idx} " + " ".join(hidden_row))
            else:
                print(f"{idx} " + " ".join(row))

    def place_ships(self, num_ships):
        """
        Method to place ships randomly on the board
        """
        while len(self.ships) < num_ships:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in self.ships:
                self.ships.append((row, col))
                self.board[row][col] = "@"  # Mark ship location 
    
    def valid_guess(self, row, col):
        """
        Method to check if a given guess is valid, row and column must be greater than zero and less than the size.
        """
        return 0 <= row < self.size and 0 <= col < self.size

    def add_guess(self, row, col):
        """
        Method to add the guess to the set of guesses.
        """
        self.guesses.add((row, col))
    
    def already_guessed(self, row, col):
        """
        Method to check if the row and columns were already guessed, by comparing with guesses data set.
        """
        return (row, col) in self.guesses
    
    
    def mark(self, row, col, hit):
        """
        Method to mark a hit with "X"  or miss with "O"  on the board
        """
        if hit:
            self.board[row][col] = "X"  
        else:
            self.board[row][col] = "O"  


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
    
    def get_valid_input(self,prompt ):
        """
        Method to valid the row and column guess
        """
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value < self.size:
                    return value
                else:
                    print(f"Please enter a number between 0 and {self.size - 1}.")
            except ValueError as e:
                print(f"Invalid data: {e}. Please enter a valid integer.\n")

    def start_game(self):
        """
        Method to play the game
        """ 
        # Place ships on both boards
        self.player_board.place_ships(self.num_ships)
        self.computer_board.place_ships(self.num_ships)

        print("\nLet's play Battleships!")
        print(f"You have chosen the board size: {self.size}x{self.size}. You need to defeat {self.num_ships} ships.") 

        # Main game loop
        while self.hits < self.num_ships and self.attempts < self.max_attempts:
            self.show_boards()  # Show both boards
            # Receive and validate row and column inputs
            row = self.get_valid_input("Enter Row of your guess: ")
            col = self.get_valid_input("Enter Column of your guess: ")
            # Check if the player already guessed these coordinates
            if self.computer_board.already_guessed(row, col):
                print("You've already guessed these row and column! Try again.")
                continue
            # Add the guess to the set of guessed coordinates
            self.computer_board.add_guess(row, col)
            self.attempts += 1
 
def main():
    """
    Run the Game
    """
    startbattle = BattleshipGame()
    startbattle.start_game()
    """
    startbattle.player_board.place_ships(startbattle.num_ships)
    startbattle.computer_board.place_ships(startbattle.num_ships)
    startbattle.show_boards()
    a= int(input("Enter the row guess\n"))
    b= int(input("Enter the col guess\n"))
    print(startbattle.player_board.valid_guess(a,b))
    startbattle.player_board.add_guess(a,b)
    print(startbattle.player_board.guesses)
    startbattle.computer_board.mark(a,b,True)
    startbattle.show_boards()
    """

print("Welcome to Battleship Game")
main()
