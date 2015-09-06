import scipy as sp
import matplotlib.pyplot as plt


class GraphPlotter:
    NUMBER_OF_POINTS = 100

    def __init__(self):
        self.functions = []

    def add_function(self, f, desc):
        """Adds the function to graph plotter's list of functions"""
        self.functions.append((f, desc))

    def plot_together(self, x_from, x_to):
        """Display a single window with all functions plotted on one plot"""
        for i in range(len(self.functions)):
            self.__plot(i, x_from, x_to)
        plt.show()

    def plot_one_by_one(self, x_from, x_to):
        """Plots each function on a separate plot in separate window"""
        for i in range(len(self.functions)):
            self.__plot(i, x_from, x_to)
            plt.show()

    def plot_on_grid(self, x_from, x_to):
        """Plots the functions on separate plots but in one window"""
        k = len(self.functions)
        q = int(sp.sqrt(k))
        if k == q**2:
            rows = q
            cols = q
        elif (q + 1)*q >= k:
            rows = q + 1
            cols = q
        else:
            rows = cols = q + 1

        for i in range(len(self.functions)):
            plt.subplot(rows, cols, i + 1)
            self.__plot(i, x_from, x_to)
        plt.show()


    def __plot(self, index, x_from, x_to):
        xx = sp.linspace(x_from, x_to, self.NUMBER_OF_POINTS)
        yy = self.functions[index][0](xx)
        plt.plot(xx, yy, label=self.functions[index][1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc=4)
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')
        plt.grid()

def cube(x):
    return x**3

def square(x):
    return x**2

def lin(x):
    return 3*x + 5

def lin2(x):
    return -2*x

def lin3(x):
    return 0.1*x + 10

def mylog(x):
    return 1/(sp.log(abs(x) - 5))

g = GraphPlotter()
g.add_function(square, 'square')
g.add_function(lin, '3x + 5')
g.add_function(cube, 'cube')
g.add_function(lin2, '-2x')
g.add_function(lin3, '0.1x + 10')
g.add_function(mylog, '1/log(|x| - 5)')
g.plot_together(-5, 5)
g.plot_one_by_one(-10, 10)
g.plot_on_grid(-10, 10)