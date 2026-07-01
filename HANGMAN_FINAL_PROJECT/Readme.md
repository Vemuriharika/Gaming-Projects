# Hangman Game 

## Project Overview

This project is a console-based implementation of the classic **Hangman Game** developed using **Python**. The game challenges players to guess a randomly selected English word by entering one letter at a time. Each incorrect guess reduces the player's remaining lives, and the game visually displays the hangman using ASCII art until the player either guesses the word correctly or runs out of attempts.

The project demonstrates fundamental Python programming concepts, including loops, conditional statements, functions, lists, string manipulation, and external library integration.



## Objectives

* Develop an interactive command-line Hangman game.
* Practice Python programming fundamentals.
* Implement game logic using loops and conditional statements.
* Utilize external libraries for random word generation.
* Improve problem-solving and debugging skills.



## Technologies Used

* Python 3
* NLTK (Natural Language Toolkit)
* Random Module



## Dataset

The project uses the **English Words Corpus** from the NLTK library.

The corpus provides thousands of English words, from which a random word is selected at the start of each game.



## Features

* Random word selection using the NLTK Words Corpus.
* Interactive command-line gameplay.
* ASCII-based Hangman illustrations.
* Six lives for each game.
* Tracks previously guessed letters.
* Displays the current progress of the hidden word.
* Prevents duplicate guesses.
* Displays the correct word when the player loses.
* Win and lose messages based on game outcome.



## Project Structure


Hangman-Game/

│

├── hangman_project.py

├── hangman_art.py

├── Readme.md


## How the Game Works

1. A random English word is selected from the NLTK Words Corpus.
2. The word is displayed as underscores representing each letter.
3. The player guesses one letter at a time.
4. If the guessed letter is correct:

   * The letter is revealed in its correct position(s).
5. If the guessed letter is incorrect:

   * One life is deducted.
   * The Hangman illustration is updated.
6. The game continues until:

   * The player correctly guesses the entire word, or
   * All six lives are exhausted.



## Game Flow

* Start the game.
* Display the hidden word.
* Accept user input.
* Validate the guessed letter.
* Update the displayed word.
* Update remaining lives.
* Display the Hangman stage.
* Determine whether the player wins or loses.



## Skills Demonstrated

* Python Programming
* Object-Oriented Thinking
* Control Flow
* Loops
* Conditional Statements
* Lists and Strings
* Randomization
* User Input Handling
* Debugging
* Problem Solving



## Installation

### Clone the Repository

git clone https://github.com/Vemuriharika/Hangman-Game.git


### Install NLTK


pip install nltk


### Download the Words Corpus


import nltk
nltk.download('words')


### Run the Game


python hangman_project.py

## Sample Gameplay


Word to guess: _______

Guess the letter: a

Word to guess: _ a _ _ _ _ _

Lives Remaining: 6

Guess the letter: z

You guessed 'z' is not in the word.

Lives Remaining: 5

      +---+
      |   |
      0   |
          |
          |
          |
=============


## Learning Outcomes

Through this project, I gained practical experience in:

* Developing interactive console applications.
* Managing game states and user interactions.
* Working with Python libraries.
* Handling user input and validation.
* Implementing game logic efficiently.
* Writing clean and readable Python code.



## Future Enhancements

* Add difficulty levels (Easy, Medium, Hard).
* Categorize words (Animals, Countries, Technology, etc.).
* Display hints for each word.
* Implement score tracking.
* Add timer-based gameplay.
* Build a graphical user interface using Tkinter or Pygame.
* Package the game as a standalone executable.




