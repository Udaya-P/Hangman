# Hangman

**Hangman** is a classic word-guessing game where you try to guess a hidden word by suggesting letters. With each incorrect guess, a part of the hangman is drawn. The game continues until you either guess the word correctly or the hangman is fully drawn, indicating a loss.

## Features

- **Word Guessing**: Guess letters to reveal the hidden word.
- **Hangman Drawing**: A part of the hangman figure is drawn for each incorrect guess.
- **Game Over Conditions**: The game ends when the word is guessed correctly or the hangman is fully drawn.

## Game Mechanics

1. **Guessing Letters**: Input a letter to guess if it is part of the hidden word.
2. **Letter Placement**: If the guessed letter is in the word, it will be revealed in its correct position(s).
3. **Incorrect Guesses**: Each incorrect guess results in a part of the hangman being drawn. There are typically 6 parts:
   - Head
   - Body
   - Left arm
   - Right arm
   - Left leg
   - Right leg
4. **Winning and Losing**: The game is won if all letters of the word are guessed correctly before the hangman is fully drawn. The game is lost if the hangman is fully drawn before the word is guessed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Udaya-P/hang_man.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hang_man
    ```

## Usage

1. Run the Hangman program.
2. Enter a letter to guess.
3. The program will display the updated word with guessed letters and draw parts of the hangman for incorrect guesses.
4. Continue guessing until you either win or lose.

## Example
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    
Guess a letter: v
v _ _ _ _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: s
v _ _ _ _ _ _ s _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: u 
v _ _ _ u _ _ s _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: r
v _ _ _ u r _ s _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: i
v _ _ _ u r i s _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: s
You've already guessed s
v _ _ _ u r i s _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: f
Letter not in word!, You lose a life
v _ _ _ u r i s _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: a
Letter not in word!, You lose a life
v _ _ _ u r i s _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: c
Letter not in word!, You lose a life
v _ _ _ u r i s _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: s
You've already guessed s
v _ _ _ u r i s _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: m
v _ _ _ u r i s m

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: o
v o _ _ u r i s m

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: b
Letter not in word!, You lose a life
v o _ _ u r i s m

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Guess a letter: n
Letter not in word!, You lose a life
v o _ _ u r i s m

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: l
Letter not in word!, You lose a life
You lose
The word was voyeurism
v o _ _ u r i s m

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
