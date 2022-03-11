from colorama import init
from src.deck import Deck
from src.board import Board
from src.err import make_log
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
    try:
        ui.main_loop()
        renderer.draw()

    except Exception as e:
        make_log(e, ui)
        raise Exception(e)