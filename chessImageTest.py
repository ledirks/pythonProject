
import chess.svg
from stockfish import Stockfish
# from wand.image import Image
# from wand.display import display
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# stockfish = Stockfish("/usr/local/Cellar/stockfish/14/bin/stockfish")
stockfish = Stockfish(r"C:\Users\david\Downloads\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe")

stockfish.make_moves_from_current_position([stockfish.get_best_move()])
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
stockfish.make_moves_from_current_position([stockfish.get_best_move()])
board = chess.Board(stockfish.get_fen_position())
svg = chess.svg.board(board, size=1500)
with open("svgFile.SVG", "w+") as svgFile:
    svgFile.write(svg)
    drawing = svg2rlg("svgFile.SVG")
    print(drawing)
    renderPM.drawToFile(drawing, "my.png", fmt="PNG")



# with Image(blob = svg, format="svg") as image: 
#     png_image = image.make_blob("png")
#     with open(deez2.png, "wb") as out:
#         out.write(png_image)