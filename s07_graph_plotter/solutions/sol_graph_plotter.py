__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy as sp
import matplotlib.pyplot as plt
import math

# ---------------------------------------------------------------
# Class
# ---------------------------------------------------------------


class GraphPlotter:
    """We can add functions to the graph plotter so that we can plot and show them.

     One by one, together in one plot or in one window but separate plots"""
    # ---------------------------------------------------------------
    # Constants
    # ---------------------------------------------------------------

    COLORS = [
        'gray',
        'blue',
        'red',
        'green',
        'orange',
        'brown',
        'violet'
    ]
    MAX_FUNCTIONS = len(COLORS)
    PTS_PER_PLOT = 100

    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self):
        self._functions = []

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def add_function(self, function, name="untitled"):
        """Adds a new function (with some name) to the graph plotter"""
        if len(self._functions) >= self.MAX_FUNCTIONS:
            raise Exception("Reached max. number of functions")

        self._functions.append((function, name))

    def plot_on_grid(self, x_from=-1, x_to=1, y_from=None, y_to=None):
        """Plots each function in a separate plot, but displays all the plots in one window"""
        grid_cols = grid_rows = math.ceil(math.sqrt(len(self._functions)))
        if grid_cols*(grid_rows - 1) >= len(self._functions):
            grid_rows -= 1

        f = plt.figure(figsize=(40/grid_cols, 30/grid_rows))  # change the size of the picture
        f.subplotpars.update(wspace=0.5, hspace=0.5)  # put some more space between plots on the grid

        for i in range(len(self._functions)):
            plt.subplot(grid_rows, grid_cols, i + 1)
            self.__plot(i, x_from, x_to, y_from, y_to)

        plt.show()

    def plot_together(self, x_from=-1, x_to=1, y_from=None, y_to=None):
        """Plots all the functions together in one plot and one window"""
        for i in range(len(self._functions)):
            self.__plot(i, x_from, x_to, y_from, y_to)

        plt.show()

    def plot_one_by_one(self, x_from=-1, x_to=1, y_from=None, y_to=None):
        """Plots each function in a separate plot, displayed, one by one, each in its own window"""
        for i in range(len(self._functions)):
            self.__plot(i, x_from, x_to, y_from, y_to)
            plt.show()

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __plot(self, j, x_from, x_to, y_from, y_to):
        """Makes a plot for the j-th function on the interval x_from .. x_to.

        y_from and y_to may be specified or None, in which case optimal values will be determined
        """
        # get the function and its name
        function = self._functions[j][0]
        name = self._functions[j][1]

        # plot the function - but beware of points where can't be computed
        x_points_to_try = sp.linspace(x_from, x_to, self.PTS_PER_PLOT)
        x_points = []
        y_points = []
        first_plot = True

        def plot_what_we_have():
            nonlocal first_plot
            if len(x_points) != 0:
                plt.plot(x_points, y_points, '-', color=self.COLORS[j], label=(name if first_plot else None))
                if first_plot:
                    first_plot = False

        for x in x_points_to_try:
            # noinspection PyBroadException
            try:
                y = function(x)
                x_points.append(x)
                y_points.append(y)
            except Exception:
                plot_what_we_have()
                x_points.clear()
                y_points.clear()
        plot_what_we_have()

        # set limits, labels, grid, legend ...
        if y_from is not None and y_to is not None:
            plt.ylim(y_from, y_to)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(y=0, color='black')  # show the X-axis
        plt.axvline(x=0, color='black')  # show the Y-axis
        plt.legend(loc=4)  # bottom right corner
        plt.xlim(x_from, x_to + (x_to - x_from)/2)  # specifies the viewport of our plot
        plt.grid()

# ---------------------------------------------------------------
# Neuroscience example
# ---------------------------------------------------------------

POTASSIUM = 'K'
SODIUM = 'Na'
CHLORIDE = 'Cl'
IONS = [POTASSIUM, SODIUM, CHLORIDE]

F = 9.648*(10**4)  # Faraday's constant (C mol^-1)
R = 8.314  # Gas constant (J K^-1 mol^-1)
T = 279.45  # Temperature (K)

VALENCY = {POTASSIUM: 1, SODIUM: 1, CHLORIDE: -1}  # Valency (no units)
PERM = {POTASSIUM: 1*10**(-2), SODIUM: 0.03*10**(-2), CHLORIDE: 0.001}  # Permeability (mol cm^-2 s^-1)
CONC_IN = {POTASSIUM: 400*10**(-6), SODIUM: 50*10**(-6), CHLORIDE: 40*10**(-6)}  # Inside concentration (mol cm^-3)
CONC_OUT = {POTASSIUM: 20*10**(-6), SODIUM: 440*10**(-6), CHLORIDE: 560*10**(-6)}  # Outside concentration (mol cm^-3)


def current_density(ion, voltage):
    left = PERM[ion]*(VALENCY[ion]**2)*(F**2)*voltage/(R*T)
    exp_part = sp.exp(-VALENCY[ion]*F*voltage/(R*T))
    nominator = CONC_IN[ion] - CONC_OUT[ion]*exp_part
    denominator = 1 - exp_part

    return left*(nominator/denominator)


def neuroscience():
    g = GraphPlotter()
    g.add_function(lambda x: current_density(POTASSIUM, x), POTASSIUM)
    g.add_function(lambda x: current_density(SODIUM, x), SODIUM)
    g.add_function(lambda x: current_density(CHLORIDE, x), CHLORIDE)
    g.plot_together(-0.1, 0.1)
    g.plot_one_by_one(-0.1, 0.1)
    g.plot_on_grid(-0.1, 0.1)


# ---------------------------------------------------------------
# Other example
# ---------------------------------------------------------------


def square(x):
    return x**2


def log_10_x(x):
    return math.exp(x**(1/5))


def primes(x):
    return x/math.log(x)


def example():
    g = GraphPlotter()
    # g.add_function(square, "square of x")
    # g.add_function(log_10_x, "log_10(x)")
    g.add_function(primes, "~π(x)")
    g.add_function(lambda x: 1/x, "1/x")
    g.add_function(lambda x: 1/math.log(abs(x) - 5), "1/log(|x| - 5)")
    g.add_function(lambda x: x**3, "x cubed")
    g.add_function(lambda x: x**4, "x^4")
    g.add_function(lambda x: math.exp(x), "exp(x)")
    g.add_function(lambda x: math.exp(math.sqrt(abs(x))), "e^(sqrt(|x|))")
    # g.plot_together(-10, 10)
    # g.plot_together(-1, 1)
    # g.plot_one_by_one(-10, 10)
    g.plot_on_grid(-10, 10)


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    example()
    #neuroscience()

if __name__ == "__main__":
    main()