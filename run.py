from colorama import init
from src.deck import Deck
from src.board import Board
from src.renderer import Renderer
from src.userinterface import UserInterface

init(autoreset=True) # colorama

deck = Deck()
board = Board()
ui = UserInterface(board)
renderer = Renderer(board, ui)


board.deal(deck, shuffle=True)
renderer.draw()

while True:
    ui.main_loop()
    renderer.draw()