# Task 1 - Hangman Game

## Overview
A console-based Hangman word-guessing game built in Python. The program randomly selects a secret word, and the player must guess it one letter at a time before running out of allowed wrong guesses.

## How It Works
- A word is randomly chosen from a predefined list (`python`, `algorithm`, `variable`, `function`, `keyboard`).
- The player guesses one letter at a time.
- Correctly guessed letters are revealed in the word display; incorrect guesses reduce the remaining attempts.
- The player has a maximum of **6** wrong guesses before the game ends.
- The game shows:
  - The current state of the word (guessed letters revealed, others as `_`)
  - Number of wrong guesses remaining
  - Letters already guessed incorrectly
- The game ends in a **win** (word fully guessed) or a **loss** (wrong guesses reach the limit).

## File
- `Task1.py` - Main game script.

## How to Run
```bash
python Task1.py
```

## Sample Gameplay
```
Welcome to Hangman!
The word has 6 letters.

Word: _ _ _ _ _ _
Wrong guesses left: 6
Missed: 
Guess a letter: p
✅ Good guess!
```

## Notes
- Input is validated to accept only single alphabetic characters.
- Duplicate guesses are detected and the player is prompted again.
- No external libraries are used; only Python's built-in `random` module.
