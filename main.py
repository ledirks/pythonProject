# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from stockfish import Stockfish

stockfish = Stockfish("/usr/local/Cellar/stockfish/14/bin/stockfish")

print(stockfish.get_board_visual())
move = str(input("User move, reset, quit:"))

while move != "quit":
    if move == "reset":
        stockfish.set_position()
        print(stockfish.get_board_visual())
        move = str(input("User move, quit:"))
        if move == "quit":
            break;

    if not stockfish.is_move_correct(move):
        print("Bad Move")

    else:
        tempL = [move]
        stockfish.make_moves_from_current_position(tempL)
        move = stockfish.get_best_move()

        if str(move) == 'None':
            print(stockfish.get_board_visual())
            print("White Wins, wtf how? Doesn't matter wasn't even trying. (╯°□°）╯︵ ┻━┻")
            break

        tempL = [move]
        stockfish.make_moves_from_current_position(tempL)

    print(stockfish.get_board_visual())
    if str(stockfish.get_best_move()) == 'None':
        print("Black Wins, YEEEEEEAAAZZZZ (° ͜ʖ͡°)╭∩╮")
        break

    move = str(input("User move, reset, quit:"))

