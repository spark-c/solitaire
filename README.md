# solitaire

An in-line/text Solitaire (3-Card Klondike) game!

Written by Collin Sparks using Python 3.10.1

---

I moved house from Illinois to Ohio at the end of November, and I didn't have internet access for about two weeks. I played a bunch of board/card games in that time -- including a bunch of Solitaire. I eventually got bored of the cards, so naturally... I'm writing my own Solitaire game!

~~Everything~~ Almost everything* is written using the standard Python library, including a test suite using `unittest`.

*I did include the use of [`colorama`](https://pypi.org/project/colorama/) to handle colored text in the terminal.

Here's a look at the game board right now (copy-pasted from terminal; browsers may disrupt text alignment):
```
 | ------- | ------- | ------- | ------- | ------- | ------- | ------- | 
 | < ??? > |         |         |    8    |    9    |    0    |    -    | 
 | < ??? > |         |         |  [Ace]  |  [Ace]  |  [Ace]  |  [Ace]  | 
 | < ??? > |         |         |         |         |         |         | 
 |         |         |         |         |         |         |         | 
 | ------- | ------- | ------- | ------- | ------- | ------- | ------- | 
 | < 5 ♠ > | < ??? > | < ??? > | < ??? > | < ??? > | < ??? > | < ??? > | 
 |         | < 7 ♠ > | < ??? > | < ??? > | < ??? > | < ??? > | < ??? > | 
 |         |         | < K ♥ > | < ??? > | < ??? > | < ??? > | < ??? > | 
 |         |         |         | < 5 ♥ > | < ??? > | < ??? > | < ??? > | 
 |         |         |         |         | < A ♦ > | < ??? > | < ??? > | 
 |         |         |         |         |         | < Q ♠ > | < ??? > | 
 |         |         |         |         |         |         | < Q ♦ > | 
 |         |         |         |         |         |         |         | 
 |    1    |    2    |    3    |    4    |    5    |    6    |    7    | 
 | ------- | ------- | ------- | ------- | ------- | ------- | ------- | 
Select waste with w     Select tableau with 1234567     Select foundations with 890-
Flip stock: s   Move card with 'src dest [amt=1]'

Enter move: 

```

The user controls the cards by typing commands that reference the columns (tableaus) from/to which the card will move, and the number of cards to move with that command. They may flip the next three cards over from the stock pile into the waste pile with the command "s", and then the available waste cards can be accessed like any other tableau column, with "w" as a reference.

I'm currently finishing bug-squashing the game logic, and then I'll move on to adding a nice little main-menu and finishing touches.

## Installation

1. Clone this repo with `git clone https://github.com/spark-c/solitaire`
1. Navigate to the project root with `cd solitaire`
1. /src contains the source code. /tests contains the tests.
1. The game is started with `py -m run` on Windows; `python3 -m run` for Linux.
