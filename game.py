from tictactoe.board import TicTacToeBoard


board = TicTacToeBoard()

current_player = "o"

while board.who_won() == "" and not board.is_full():
    moved = False
    current_player = "o" if current_player == "x" else "x"
    while not moved:
        print("player = " + current_player)
        x, y = 0, 0
        while not 0 < x < 4:
            x = int(input("x? "))
        while not 0 < y < 4:
            y = int(input("y? "))
        x -= 1
        y -= 1
        moved = board.do_move(x, y, current_player == "x")
        if moved:
            board.print_board()
        else:
            print("Invalid move!")

if board.is_full():
    print("== TIE ==")
else:
    print("== PLAYER " + board.who_won() + " WON!")

