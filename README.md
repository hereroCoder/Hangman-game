
# Hangman Game in Python

This is a simple Hangman game implemented in Python. Hangman is a word-guessing game where the player must guess a hidden word letter by letter. With each incorrect guess, a part of a hangman is drawn. The player has a limited number of attempts to guess the word correctly before the hangman is fully drawn.

## How the Game Works

### Game Logic

1. A random word is selected from a predefined list.
2. A row of blank spaces is displayed, each representing a letter in the selected word.
3. The player guesses letters to fill in the blanks.
4. If a guessed letter is in the word, it is revealed in the correct blank spaces.
5. If a guessed letter is not in the word, a part of the hangman is drawn, and the player loses a life.
6. The game continues until the player correctly guesses the word or the hangman is fully drawn, leading to a loss.

### Don't Penalize More Than Once

The game ensures that the player is penalized only once for guessing a wrong letter, even if the same letter is guessed multiple times.

The game keeps track of previously guessed characters and displays them for the player to see.

## How to Play

1. Clone the repository to your local machine.
2. Ensure you have Python 3 installed.
3. Open your terminal or command prompt and navigate to the project directory.
4. Run the game by executing `python hangman.py`.


## Future Improvements

You can enhance the game by adding multiple difficulty levels (easy, medium, hard) to provide a more challenging experience for players.

## Contribution

Contributions to this project are welcome! If you'd like to improve the game, add new features, or provide bug fixes, please open an issue or submit a pull request.


Have fun playing Hangman!
