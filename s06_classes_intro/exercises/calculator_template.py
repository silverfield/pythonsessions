# ---------------------------------------------------------------
# Class - Calculator
# ---------------------------------------------------------------


class Calculator:
    """Simple calculator that remembers what it was doing"""
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self):
        pass

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def add(self, a, b):
        """Computes the addition and stores the result"""
        pass

    def subtract(self, a, b):
        """Computes the subtraction and stores the result"""
        pass

    def multiply(self, a, b):
        """Computes the multiplication and stores the result"""
        pass

    def divide(self, a, b):
        """Computes the division and stores the result"""
        pass

    def clear(self):
        """Clears the history of calculations as well as result"""
        pass

    def print_result(self):
        """Prints the result of last operation"""
        pass

    def print_history(self):
        """Prints the history of calculations"""
        pass

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


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

# Output of the above should be:

# Result is: 16.0
# History of calculations
# 	5 + 6 = 11
# 	11 - 7 = 4
# 	4 * 2 = 8
# 	8 / 0.5 = 16.0
# Result is: None
# Result is: 1
# History of calculations
# 	0 + 1 = 1

if __name__ == '__main__':
    main()
