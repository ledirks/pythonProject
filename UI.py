from tkinter import *
from stockfish import Stockfish
import serial
import aioconsole
import asyncio
import chess.svg
from PIL import ImageTk, Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
# stockfish = Stockfish("/usr/local/Cellar/stockfish/14/bin/stockfish")
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
# img = Image.open("my.png")
# resized_img = img.resize((500, 500))
# img = ImageTk.PhotoImage(resized_img)

# svg = chess.svg.board(chess.Board(stockfish.get_fen_position()), size=1500)
# with open("svgFile.SVG", "w+") as svgFile:
#     svgFile.write(svg)
#     drawing = svg2rlg("svgFile.SVG")
#     print(drawing)
#     renderPM.drawToFile(drawing, "my.png", fmt="PNG")
# img = ImageTk.PhotoImage(Image.open("my.png"))

class Board:
    board: Text
    def __init__(self):
        # self.board = Text(root, width=45, height=20)
        self.board = Label(root, image=None)


    def draw(self):
        print('hi')
        svg = chess.svg.board(chess.Board(stockfish.get_fen_position()), size=1500)
        with open("svgFile.SVG", "w+") as svgFile:
            svgFile.write(svg)
            drawing = svg2rlg("svgFile.SVG")
            renderPM.drawToFile(drawing, "my.png", fmt="PNG")
        img = Image.open("my.png")
        resized_img = img.resize((500, 500))
        img = ImageTk.PhotoImage(resized_img)
        # img = ImageTk.PhotoImage(Image.open("my.png"))
        self.board.configure(image=img)
        self.board.image = img
        self.board.pack(side=LEFT)
        # self.board.delete('1.0', END)
        # self.board.insert('1.0', "  A   B   C   D   E   F   G   H\n")
        # self.board.insert('1.0', stockfish.get_board_visual())
        # self.board.pack(side=TOP)

def player_forfeit():
    print('\n╭∩╮(° ͜ʖ͡°)╭∩╮ you lose ╭∩╮(° ͜ʖ͡°)╭∩╮')
    global game_over
    game_over = True
    forfeitButton["state"] = "disabled"
    message.set("╭∩╮(° ͜ʖ͡°)╭∩╮ you lose ╭∩╮(° ͜ʖ͡°)╭∩╮")

def player_hint():

    message.set("Here you go nerd " + stockfish.get_best_move())

def player_reset():
    global game_over
    stockfish.set_position([])
    game_over = False
    board.draw()
    root.update()

board = Board()
forfeitButton = Button(buttonFrame, text="Forfeit", width=15, height=5, bg="black", fg="white", command=player_forfeit)
hintButton = Button(buttonFrame, text="Hint", width=15, height = 5, bg="black", fg = "white", command=player_hint)
resetButton = Button(buttonFrame, text="Reset Board", width=15, height = 5, bg="black", fg = "white", command=player_reset)
# panel = Label(image = img)
hintButton.pack(side = LEFT)
resetButton.pack(side = LEFT)
forfeitButton.pack(side = LEFT)
# panel.pack(side = LEFT)



# async wait for console input
async def getConsoleInput():
    global game_over
    move = stockfish.get_best_move()
    if str(move) == 'None':
        message.set("Black wins")
        game_over = True
        return
    move = str(input("User move: "))
    if (stockfish.is_move_correct(move)):
        stockfish.make_moves_from_current_position([str(move)])
        move = stockfish.get_best_move()
        if str(move) == 'None':
            message.set("White wins")
            game_over = True
            return
        stockfish.make_moves_from_current_position([str(move)])
    else:
        message.set("Bad move numbnuts")
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
