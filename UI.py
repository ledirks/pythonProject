from tkinter import *
import tkinter
from stockfish import Stockfish
import serial
import aioconsole
import asyncio

#stockfish = Stockfish("/usr/local/Cellar/stockfish/14/bin/stockfish")
stockfish = Stockfish(r"C:\Users\david\Downloads\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe")

game_over = False

root = Tk()
root.title("Chess")
message = StringVar()
showInfo = Label(root, textvariable=message)
message.set("No hint for now ┏(-_-)┛")
buttonFrame = Frame(root)
buttonFrame.pack(side = BOTTOM)
showInfo.pack(side = BOTTOM)

class Board:
    board: Text

    def __init__(self):
        self.board = Text(root, width=45, height=20)
        self.board.tag_configure("center")


    def draw(self):
        self.board.delete('1.0', END)
        self.board.insert('1.0', "  A   B   C   D   E   F   G   H\n")
        self.board.insert('1.0', stockfish.get_board_visual())
        self.board.pack(side=TOP)


board = Board()

def player_forfeit():
    print('\n╭∩╮(° ͜ʖ͡°)╭∩╮ you lose ╭∩╮(° ͜ʖ͡°)╭∩╮')
    global game_over
    game_over = True
    forfeitButton["state"] = "disabled"

def player_hint():

    message.set("Here you go nerd " + stockfish.get_best_move())

forfeitButton = Button(buttonFrame, text="Forfeit", width=15, height=5, bg="black", fg="white", command=player_forfeit)
hintButton = Button(buttonFrame, text="Hint", width=15, height = 5, bg="black", fg = "white", command=player_hint)
resetButton = Button(buttonFrame, text="Reset Board", width=15, height = 5, bg="black", fg = "white")
hintButton.pack(side = LEFT)
resetButton.pack(side = LEFT)
forfeitButton.pack(side = LEFT)



# async wait for console input
async def getConsoleInput():
    move = str(input("User move: "))
    if (stockfish.is_move_correct(move)):
        stockfish.make_moves_from_current_position([str(move)])
        stockfish.make_moves_from_current_position([str(stockfish.get_best_move())])
    # return [move]


async def playGame():
    global game_over
    while(not game_over):
        board.draw()
        root.update()
        await getConsoleInput()
    # stockfish.make_moves_from_current_position(await getConsoleInput())
        root.update()
    # if the game is over just display the screen still
    # TODO need to have a way to start a new game at some point
    root.mainloop()
    return


asyncio.run(playGame())
print('done')
