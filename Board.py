from tkinter import *
class Board:
    board: Text

    def __init__(self):
        self.board = Text(root, width=45, height=20)


    def draw(self):
        self.board.delete('1.0', END)
        self.board.insert('1.0', "  A   B   C   D   E   F   G   H\n")
        self.board.insert('1.0', stockfish.get_board_visual())
        self.board.pack(side=TOP)