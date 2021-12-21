# solitaire

An in-line/text Solitaire (3-Card Klondike) game!

Written by Collin Sparks using Python 3.10.1

---

I moved house from Illinois to Ohio at the end of November, and I didn't have internet access for about two weeks. I played a bunch of board/card games in that time -- including a bunch of Solitaire. I eventually got bored of the cards, so naturally... I'm writing my own Solitaire game!

Everything is written using the standard Python library, including a test suite using `unittest`.

Here's a look at the game board right now:
```
 | ------- | ------- | ------- | ------- | ------- | ------- | ------- | 
 | < ??? > |         |         |    8    |    9    |    0    |    -    | 
 | < ??? > |         |         |  [Ace]  |  [Ace]  |  [Ace]  |  [Ace]  | 
 | < ??? > |         |         |         |         |         |         |
 |         |         |         |         |         |         |         |
 | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
 | < Q ♥ > | < ??? > | < ??? > | < ??? > | < ??? > | < ??? > | < ??? > |
 |         | < 8 ♦ > | < ??? > | < ??? > | < ??? > | < ??? > | < ??? > |
 |         |         | < K ♣ > | < ??? > | < ??? > | < ??? > | < ??? > |
 |         |         |         | < 6 ♥ > | < ??? > | < ??? > | < ??? > |
 |         |         |         |         | < 2 ♥ > | < ??? > | < ??? > |
 |         |         |         |         |         | < 7 ♦ > | < ??? > |
 |         |         |         |         |         |         | < J ♥ > |
 |         |         |         |         |         |         |         |
 |    1    |    2    |    3    |    4    |    5    |    6    |    7    |
 | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
Select waste with w     Select tableau with 1234567     Select foundations with 890-
Flip stock: s   Move card with 'src dest [amt=1]'
```

The user will control the cards by typing commands that reference the columns (tableaus) from/to which the card will move, and the number of cards to move with that command. They may flip the next three cards over from the stock pile into the waste pile with the command "s", and then the available waste cards can be accessed like any other tableau column, with "w" as a reference.

I'm currently finishing up with implementing user input validation / error feedback, finishing card movement via commands (the API already exists), and then moving on to game logic.

## Installation

1. Clone this repo with `git clone https://github.com/spark-c/solitaire`
1. Navigate to the project root with `cd solitaire`
1. /src contains the source code. /tests contains the tests.
1. The game is started with `py -m run` on Windows; `python3 -m run` for Linux.
  - NOTE: The game loop is not implemented yet, so running will do only whatever happens to be in run.py at the time :)
