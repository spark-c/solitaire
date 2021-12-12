from src.deck import Deck
from src.board import Board
from src.renderer import Renderer


d = Deck()
b = Board()
r = Renderer()


b.deal(d, shuffle=False)
r._draw_header(b)