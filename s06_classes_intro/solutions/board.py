__author__ = 'ferrard'

# ---------------------------------------------------------------
# Class - Board
# ---------------------------------------------------------------


class Board:
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self._grid = None

        self.clean()

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def clean(self):
        self._grid = [[' '] * self.m for _ in range(self.n)]

    def print(self):
        print("The board content is:")
        print(str(self))

    def __str__(self):
        s = "-" * (self.m + 2)
        s += "\n"
        s += "\n".join(('|' + ''.join(row) + '|') for row in self._grid)
        s += "\n"
        s += "-" * (self.m + 2)
        return s

    def write(self, x, y, text):
        if y + len(text) >= self.m:
            print("This text will not fit on the board")
        for i in range(len(text)):
            if y + i >= self.m:
                break
            if y + i >= self.m - 3:
                self._grid[self.n - x - 1][y + i] = '.'
            else:
                self._grid[self.n - x - 1][y + i] = text[i]

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    b = Board(10, 50)
    b.write(0, 0, "Hello everyone")
    b.write(9, 30, "If x equals pi^2, then we cannot integrate f because it's not continuous")
    b.print()
    b.clean()
    b.write(0, 0, "Hello again!")
    b.print()

if __name__ == '__main__':
    main()
