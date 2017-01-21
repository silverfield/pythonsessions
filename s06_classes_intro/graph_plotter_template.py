class GraphPlotter:
    def __init__(self):
        self.functions = []

    def add_function(self, f, desc):
        """Adds the function to graph plotter's list of functions"""
        self.functions.append((f, desc))

    def plot_together(self, x_from, x_to):
        """Display a single window with all functions plotted on one plot"""
        pass

    def plot_one_by_one(self, x_from, x_to):
        """Plots each function on a separate plot in separate window"""
        pass

    def plot_on_grid(self, x_from, x_to):
        """Plots the functions on separate plots but in one window"""
        pass


def square(x):
    return x**2


def lin(x):
    return 3*x + 5

# we want 100 points from -10 .. 10
# generate values for x
import scipy as sp
xx = sp.linspace(-10, 10, 100)

# evaluate the functions at those values
yy_square = square(xx)
yy_lin = lin(xx)

# plot
import matplotlib.pyplot as plt
plt.plot(xx, yy_lin)
plt.plot(xx, yy_square)
plt.show()