class StarSquare:
    def __init__(self, n):
        self.n = n

    def print(self):
        for i in range(self.n):
            for j in range(self.n):
                print('*', end='')
            print()

    def change_n(self, new_n):
        self.n = new_n

my_first_square = StarSquare(7)
my_first_square.print()
my_first_square.change_n(5)
my_first_square.print()

my_second_square = StarSquare(2)
my_second_square.print()