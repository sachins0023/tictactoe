class TicTacToe:

    def __init__(self):
        self.game = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append('*')
            self.game.append(row)
        # print(self.game)

    def enter_xo(self, entry, pos):
        self.game[int(pos[0])][int(pos[1])] = entry
        self.display()

    def check_win(self):
        out = []
        #horizontal
        for i in range(3):
            if all(x == 'x' for x in self.game[i]) or all(x == 'o' for x in self.game[i]):
                out.append(True)
            else:
                out.append(False)

        #vertical
        for i in range(3):
            if all(x == 'x' for x in [self.game[0][i], self.game[1][i], self.game[2][i]]) or all(x == 'o' for x in [self.game[0][i], self.game[1][i], self.game[2][i]]):
                out.append(True)
            else:
                out.append(False)
        #diagonals
        diag1 = []
        diag2 = []
        for i in range(3):
            for j in range(3):
                if i==j:
                    diag1.append(self.game[i][j])
                if i+j == 2:
                    diag2.append(self.game[i][j])
        if all(x == 'x' for x in diag1) or all(x == 'o' for x in diag1):
            out.append(True)
        else:
            out.append(False)
        if all(x == 'x' for x in diag2) or all(x == 'o' for x in diag2):
            out.append(True)
        else:
            out.append(False)

        if True in out:
            return True
        else:
            return False

    def display(self):
        for i in range(3):
            print()
            for j in range(3):
                print(self.game[i][j],end = '')

match1 = TicTacToe()
match1.display()

while(1):
    match1.enter_xo(input("\nEnter x or o: "), input("\nEnter your position: ").split(','))
    if match1.check_win():
        print("game over")
        break
