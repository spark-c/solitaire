#import


class Renderer:

    def __init__(self):
        pass


    def _draw_header(self, board) -> None:
        pass


    def _draw_tableaus(self, board) -> None:
        pass


    def draw(self, board) -> None:
        rows_required: int = 4 + board.len_max_tableau


        """
        draw0
            stock
            tab0
        draw1
            waste
            tab1
        draw2
            tab2
        draw3
            tab3
            found0
        draw4
            tab4
            found1
        draw5
            tab5
            found2
        draw6
            tab6
            found3
        """

        """
        1. Find longest tableau
        2. Grid should be 7 wide x len(tableau) + 4
        Row0: stock0 waste0 5spaces
        Row1: stock1 waste1 1spaces found0 found1 found2 found3
        Row2: stock2 waste2 5spaces
        Row3: 7spaces
        """

        """
        < ?? > | < SS > |
        < ?? > | < SS > |        | < SS > | < SS > | < SS > | < SS > |
        < ?? > | < SS > |

        < SS > | < SS > | < SS > | < SS > | < SS > | < SS > | < SS > |
        """