import cairosvg
import chess.svg
from stockfish import Stockfish

stockfish = Stockfish("/usr/local/Cellar/stockfish/14/bin/stockfish")
stockfish.make_moves_from_current_position(stockfish.get_best_move())
board = chess.Board(stockfish.get_fen_position())
svg = chess.svg.board(board, size=350)
cairosvg.svg2png(bytestring=svg,write_to='output.png')

