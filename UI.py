from tkinter import *
import tkinter
from stockfish import Stockfish
import serial
import aioconsole
import asyncio
stockfish = Stockfish(r"C:\Users\david\Downloads\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe")


root = Tk()
root.title("Chess")


class Board:
    board: Text
    def __init__(self):
        self.board = Text(root, width=50, height=25)

    # def canvas_onclick(self, event):
    #     self.canvas.itemconfig(
    #         self.text_id, 
    #         text="You clicked at ({}, {})".format(event.x, event.y)
    #     )
    #     print("Balls")

    def draw(self):
        # self.canvas.move(self.id, 0, -1)
        # self.canvas.after(10, self.draw)  #(time_delay, method_to_execute)
        
        #infinitely print board without blocking other input 
        # self.board.pack(side=LEFT)
        self.board.delete('1.0',END)
        self.board.insert('1.0', "  A   B   C   D   E   F   G   H\n")
        self.board.insert('1.0', stockfish.get_board_visual())
        self.board.grid(row=0, column=0)
        self.board.after(1000, self.draw)

board = Board()

# def displayBoard():
#     board.insert('1.0', "  A   B   C   D   E   F   G   H\n")
#     board.insert('1.0', stockfish.get_board_visual())

#     root.update()



# forfeitButton = Button(text="Forfeit", width=25, height=5, bg="black", fg="white")
# hintButton = Button(text="Hint", width=25, height = 5, bg="black", fg = "white")
# undoButton = Button(text="Undo Last Move", width=25, height = 5, bg="black", fg = "white")
# makeMoveButton = Button(text="Make Move", width=25, height = 5, bg = "black", fg="white")
# entry1 = Entry(root )
# board.pack(side=LEFT)
# hintButton.pack()
# undoButton.pack()
# forfeitButton.pack()
# makeMoveButton.pack()
# entry1.pack()


# async wait for console input
async def getConsoleInput():
    return await asyncio.sleep(1, result=3)


def playGame():
    board.draw()
    
    root.mainloop()

playGame()
print('done')






