# Hangman

Hangman game implemented using Python and Turtle Graphics!

## Getting Started

Download the files above and follow the steps below.

### Installing

Open the terminal, navigate to where you want the game's files to be stored in and create a new directory:

``` bash
mkdir DIRECTORY_NAME
```

Enter the new directory:

``` bash
cd DIRECTORY_NAME
```

Create and activate a new virtual environment:

``` bash
python3 -m venv myenv
source myenv/bin/activate
```

Copy the downloaded files into the virtual environment created and enter the virtual environment:

``` bash
cd myenv
```

Run the following line to install all dependencies for the game:

``` bash
pip3 install -r requirements.txt
```

## Usage

Start the game by running this line in the terminal:

``` bash
python hangman.py words.txt
```

A turtle graphics screen will popup which is empty initially but will draw out the hangman as incorrect guesses are attempted. Enter in a letter in the terminal to make guesses.

The game is won when the word is guessed completely, or lost when the entire hangman has appeared. To end the game, type 'end' into the terminal. Good luck!

### Note

If while attempting to make a guess results in a NameError exception, ensure all letters (as well as 'end' to stop the game) are placed within single quotes.
