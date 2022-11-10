

class TicTacToeBoard:
    def __init__(self):
        self.board = [["" for i in range(3)] for j in range(3)]

    def do_move(self, x, y, is_player_a = False):
        check = "o" if is_player_a else "x"
        if self.board[x][y] == "":
            self.board[x][y] = check
            return True
        else:
            return False

    def is_full(self):
        for j in range(3):
            for i in range(3):
                if self.board[j][i] == "":
                    return False
        else:
            return True

    def who_won_by_vertical(self, x):
        if self.board[x][0] == self.board[x][1] == self.board[x][2]:
             return self.board[x][0]
        else:
            return ""

    def who_won_by_horizontal(self, y):
        if self.board[0][y] == self.board[1][y] == self.board[2][y]:
             return self.board[0][y]
        else:
            return ""

    def who_won_by_oblique_forward(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
             return self.board[0][0]
        else:
            return ""

    def who_won_by_oblique_backward(self):
        if self.board[2][0] == self.board[1][1] == self.board[0][2]:
             return self.board[2][0]
        else:
            return ""

    def who_won(self):
        to_check_boxes = [(0,0), (1,1), (2,2)]
        for to_check_box in to_check_boxes:
            return self.who_won_by_vertical(to_check_box[0]) or self.who_won_by_horizontal(to_check_box[1]) or self.who_won_by_oblique_forward() or self.who_won_by_oblique_backward()

    def print_board(self):
        for j in range(3):
            for i in range(3):
                print(" %1s " % self.board[j][i], end="")
                if i < 2:
                    print("|", end="")
                else:
                    print("")
            if j < 2:
                print("---+---+---")