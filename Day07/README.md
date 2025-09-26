Day 7 - Hangman Game
Overview

For Day 7, I created a Hangman Game in Python. The game selects a random word from a list, and the player has to guess it one letter at a time. Each wrong guess reduces the number of lives and displays a new stage of the hangman using ASCII art. The game ends when the word is guessed correctly or when all lives are lost.

Concepts Learned

Using the random module to pick a word

Lists and string manipulation to track guesses

Loops and conditionals for game flow

Modular programming by splitting code into separate files (hangman.py, hangman_words.py, hangman_art.py)

ASCII art for visual feedback

Project Structure

hangman.py - main game logic

hangman_words.py - word list

hangman_art.py - ASCII art and logo