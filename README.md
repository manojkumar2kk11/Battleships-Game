# Purpose
  Battleship game, players take turns guessing rows and columns on a board, aiming to destroy hidden ships. The board, represented by symbols, shows guesses and ship locations. Players place ships, and correct guesses mark hits. The game ends when all ships are destroyed.

  The Battleship game developed on the Python platform using the Code Institute template

# Responsive 
Responsive screen image for the different device, used https://ui.dev/amiresponsive website to capture the image. 

![Responsive screen](assets/images/responsive_read.png)

# How to Play the Battleship Game:
## Board Setup:
The game begins with you selecting a board size between 5x5 and 8x8.
Both you (the player) and the computer place ships randomly on your respective boards. You cannot see the computer’s ships, but you can see your own.
## Taking Turns:
On each turn, you guess the location of a hidden ship on the computer's board by entering a row and column number.
The computer will also randomly guess locations on your board.
## Game Objective:
The goal is to sink all of the computer's ships by correctly guessing their positions.
You win the game by hitting all the computer’s ships before the computer sinks all of yours or before your maximum number of attempts is reached.
## Symbols Used in the Game:
### $ (Default Symbol):
This is the symbol used to represent the empty spaces on the board where no guesses have been made yet.
### @ (Ship Symbol):
On your board, this symbol represents where your ships are located.
On the computer's board, you will not see this symbol unless ships are revealed at the end of the game.
### X (Hit):
This symbol appears on the board when a player guesses a location where a ship is present, indicating a successful hit.
### O (Miss):
This symbol is used when a player guesses a location where no ship is present, indicating a miss.
## Example Playthrough:
- You are prompted to enter guesses for row and column values.
- If you guess correctly, you’ll see an X marking the hit on the board.
- If you guess incorrectly, an O marks the missed attempt.
- The computer also takes turns guessing positions on your board.
- The game continues until all ships are destroyed or the maximum number of attempts is reached.