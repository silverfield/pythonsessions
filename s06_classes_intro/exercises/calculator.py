__author__ = 'ferrard'

# ---------------------------------------------------------------
# Class - Calculator
# ---------------------------------------------------------------


class Calculator:
    """Simple calculator that remembers what it was doing"""
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self):
        self.result = None
        self._history = []

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def add(self, a, b):
        """Computes the addition and stores the result"""
        self.result = a + b
        self._history.append(str(a) + " + " + str(b) + " = " + str(self.result))

    def subtract(self, a, b):
        """Computes the subtraction and stores the result"""
        self.result = a - b
        self._history.append(str(a) + " - " + str(b) + " = " + str(self.result))

    def multiply(self, a, b):
        """Computes the multiplication and stores the result"""
        self.result = a * b
        self._history.append(str(a) + " * " + str(b) + " = " + str(self.result))

    def divide(self, a, b):
        """Computes the division and stores the result"""
        self.result = a / b
        self._history.append(str(a) + " / " + str(b) + " = " + str(self.result))

    def clear(self):
        """Clears the history of calculations as well as result"""
        self.result = None
        self._history.clear()

    def print_result(self):
        """Prints the result of last operation"""
        print("Result is: " + str(self.result))

    def print_history(self):
        """Prints the history of calculations"""
        print("History of calculations")
        for h in self._history:
            print("\t" + h)

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    c = Calculator()
    c.add(5, 6)
    c.subtract(c.result, 7)
    c.multiply(c.result, 2)
    c.divide(c.result, 0.5)
    c.print_result()
    c.print_history()

    c.clear()
    c.print_result()

    c.add(0, 1)
    c.print_result()
    c.print_history()

if __name__ == '__main__':
    main()