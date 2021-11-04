from tkinter import *
from stockfish import Stockfish

stockfish = Stockfish(r"C:\Users\david\Downloads\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe")


root = Tk()
root.title("Chess")

label1 = Label(text=stockfish.get_board_visual(), fg="white", bg="black", width=50, height=25)
forfeitButton = Button(text="Forfeit", width=25, height=5, bg="black", fg="white")
hintButton = Button(text="Hint", width=25, height = 5, bg="black", fg = "white")
undoButton = Button(text="Undo Last Move", width=25, height = 5, bg="black", fg = "white")
entry1 = Entry(root)
label1.pack(side=LEFT)
hintButton.pack()
undoButton.pack()
forfeitButton.pack()
entry1.pack()
root.mainloop()