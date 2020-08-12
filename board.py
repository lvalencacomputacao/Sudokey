class Board:

    solvedBoard = [[0 for i in range(9)] for j in range(9)]
    gameRunning = True
    win = False

    def __init__(self):
        self.tabuleiro = [[0 for i in range(9)] for j in range(9)]
        self.fl = 0
        self.fc = 0

    def findFirst(self):
        for i in range(9):
            for j in range(9):
                if (not self.tabuleiro[i][j]):
                    self.fl = i
                    self.fc = j
                    return

    def reset(self):
        self.tabuleiro = [[0 for i in range(9)] for j in range(9)]
        self.gameRunning = True

    def show(self):
        for i in self.tabuleiro:
            for j in i:
                print(j, end = ' ')
            print('')

    def setCell(self, linha, coluna, valor):
        if (self.checkMove(linha, coluna, valor)):
            self.tabuleiro[linha][coluna] = valor
        else:
            print("no")

    def isFull(self):
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] == 0:
                    return False
        return True

    def numberPossibilities(self, linha, coluna):
        possible = [1 for i in range(10)]

        #horizontal check
        for col in range(9):
            if self.tabuleiro[linha][col]:
                possible[self.tabuleiro[linha][col]] = 0

        #vertical check
        for line in range(9):
            if self.tabuleiro[line][coluna]:
                possible[self.tabuleiro[line][coluna]] = 0

        #mini square check
        linhaSquare = (linha // 3) * 3
        colunaSquare = (coluna // 3) * 3
        for l in range(linhaSquare, linhaSquare + 3):
            for c in range(colunaSquare, colunaSquare + 3):
                if self.tabuleiro[l][c]:
                    possible[self.tabuleiro[l][c]] = 0

        toTry = []
        for k in range(1, 10):
            if possible[k]:
                toTry.append(k)

        return toTry

    def checkMove(self, linha, coluna, numero):

        if numero == 0:
            return True

        for i in range(9):
            if self.tabuleiro[linha][i] == numero and (linha, i) != (linha, coluna):
                print(linha, coluna)
                print(linha, i)
                print("Falso")
                return False
            if self.tabuleiro[i][coluna] == numero and (i, coluna) != (linha, coluna):
                print(i, coluna)
                print("Falso 2")
                return False
        lq = (linha // 3) * 3
        cq = (coluna // 3) * 3
        for i in range(lq, lq + 3):
            for j in range(cq, cq + 3):
                if (self.tabuleiro[i][j] == numero and (i, j) != (linha, coluna)):
                    return False
        return True

    def solve(self):
        self.show()
        print('')
        #print(self.fl, self.fc)
        #print('')
        if self.isFull():
            for i in range(9):
                for j in range(9):
                    self.solvedBoard[i][j] = self.tabuleiro[i][j]
            self.gameRunning = False
            self.tabuleiro = self.solvedBoard
            self.win = True
        elif self.gameRunning:
            found = False
            linha = 0
            coluna = 0
            for i in range(9):
                for j in range(9):
                    if (not self.tabuleiro[i][j]):
                        linha = i
                        coluna = j
                        found = True
                        break
                if found:
                    break
            numbers = self.numberPossibilities(linha, coluna)
            print(*numbers)
            print('')
            tamanho = len(numbers)
            print("here")
            for k in range(tamanho):
                if (not self.gameRunning):
                    self.tabuleiro = self.solvedBoard
                    break
                self.tabuleiro[linha][coluna] = numbers[k]
                self.solve()
            if (linha == self.fl and coluna == self.fc and not self.win):
                self.gameRunning = 0
                print("Unsolvable")
                self.reset()
            if (self.gameRunning):
                self.tabuleiro[linha][coluna] = 0
