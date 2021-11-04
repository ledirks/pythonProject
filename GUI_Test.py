#!/usr/bin/python

from tkinter import *
import stockfish
from stockfish import Stockfish


def resetgame():
    MyWindow.reset = 1


class MyWindow:
    reset = 0
    stockfish = Stockfish("/usr/local/Cellar/stockfish/14/bin/stockfish")

    def __init__(self, win):
        self.lbl1 = Label(win, text='Chess User Interface Test', font=("Courier", 25))
        self.lbl2 = Label(win, text='Current Board State')
        self.lbl3 = Label(win, text='')
        self.board = Text(win, height=200, width=200)
        self.lbl1.place(x=0, y=0)
        self.lbl2.place(x=0, y=40)
        self.lbl3.place(x=0, y=270)
        self.board.place(x=0, y=60)
        self.b1 = Button(win, text='Reset', command=resetgame)
        self.b1.place(x=0, y=350)
        self.board.insert('1.0', MyWindow.stockfish.get_board_visual())

    def getusermove(self):
        move = str(input("User move"))
        if MyWindow.reset == 1:
            MyWindow.stockfish.set_position()

        if not MyWindow.stockfish.is_move_correct(move):
            print("Bad Move")

        else:
            tempL = [move]
            MyWindow.stockfish.make_moves_from_current_position(tempL)
            move = MyWindow.stockfish.get_best_move()

            if str(move) == 'None':
                print("White Wins, wtf how? Doesn't matter wasn't even trying. (╯°□°）╯︵ ┻━┻")

            tempL = [move]
            MyWindow.stockfish.make_moves_from_current_position(tempL)

        if str(MyWindow.stockfish.get_best_move()) == 'None':
            print("Black Wins, YEEEEEEAAAZZZZ (° ͜ʖ͡°)╭∩╮")


window = Tk()
mywin = MyWindow(window)
window.title('Chess or something idk')
window.geometry("400x400+10+10")
mywin.getusermove()
mywin.board.delete('1.0', 'end')
mywin.board.insert('1.0', MyWindow.stockfish.get_board_visual())
window.mainloop()
