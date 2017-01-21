__author__ = 'ferrard'


class LeftRightDoc:
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, max_width=40):
        self._lines = []
        self._max_width = max_width

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def add_line(self, line):
        self._lines.append(line)

    def print_rl(self):
        print("Printing right-to-left:")
        for line in self._lines:
            cut_down = self.__cut_down_line_if_necessary(line)
            reveresed = self.__reverse(cut_down)
            print(reveresed)
        print()

    def print_lr(self):
        print("Printing left-to-right:")
        for line in self._lines:
            print(self.__cut_down_line_if_necessary(line))
        print()

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __reverse(self, s):
        reverse = ""
        for c in s:
            reverse = c + reverse
        return reverse

    def __cut_down_line_if_necessary(self, line):
        if len(line) > self._max_width:
            return line[:self._max_width - 3] + "..."
        return line

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    lr_doc = LeftRightDoc(40)
    lr_doc.add_line("I went to the shop today. I found biscuits, apples, bread, butter and potatoes.")
    lr_doc.add_line("But I wanted pineapples!")
    lr_doc.add_line("Next time I'll go to another shop.")
    lr_doc.print_lr()
    lr_doc.print_rl()

# output should be:
#
# Printing left-to-right:
# I went to the shop today. I found bis...
# But I wanted pineapples!
# Next time I'll go to another shop.
#
# Printing right-to-left:
# ...sib dnuof I .yadot pohs eht ot tnew I
# !selppaenip detnaw I tuB
# .pohs rehtona ot og ll'I emit txeN


if __name__ == '__main__':
    main()