__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import random

# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------

UNREVEALED = '-----'

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def play_monty_hall(doors, real_player=False):
    # create instance
    items = ['goat']*doors
    car_index = random.randint(0, doors - 1)
    items[car_index] = 'car'

    # get the guess of the user
    print("You have {} options:".format(doors))
    for i in range(doors):
        print("\t{}: {}".format(i, UNREVEALED))
    print()
    print("Where is the car?\n")
    if real_player:
        guess_index = int(input())
        while guess_index not in list(range(doors)):
            guess_index = int(input("Hey, give me number from {} to {}!".format(0, doors - 1)))
    else:
        guess_index = random.randint(0, doors - 1)
        print(guess_index)

    # select the door that would stay closed - a random index (except for guess our guess) if we guess the car, the car
    # index otherwise
    if car_index == guess_index:
        indices = list(range(doors))
        indices.remove(guess_index)
        closed_index = random.choice(indices)
    else:
        closed_index = car_index

    # reveal the doors
    print("So you think it's at {}! All right... Let's reveal som doors!".format(guess_index))
    for i in range(doors):
        print("\t{}: {}".format(i, UNREVEALED if i in [guess_index, closed_index] else items[i]), end="")
        if i == guess_index:
            print(" (your choice)")
        else:
            print()

    # ask the user if he wants to switch
    print("Do you want to switch? Yes, or no?\n")
    if real_player:
        switch_answer = input().lower()
        while switch_answer not in ["yes", "no"]:
            switch_answer = input("I said \"yes\" or \"no\"!").lower()
    else:
        switch_answer = random.choice(["yes", "no"])
        print(switch_answer)
    switched = switch_answer == "yes"
    print()

    # if he wants, switch the guess to the closed door
    if switched:
        guess_index = closed_index

    # report results
    print("So you say {}. Let's see the results!!".format(guess_index))
    for i in range(doors):
        print("\t{}: {}".format(i, items[i]), end="")
        if i == guess_index:
            print(" (your choice)")
        else:
            print()
    if guess_index == car_index:
        print("CONGRATS!!! You have a car!!!")
    elif switched:
        print("Bad luck, though I still think a switch was a good choice!!!")
    else:
        print("Sorry, perhaps switch next time? ;-)")

    return guess_index == car_index, switched


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main(argv):
    iterations = int(argv[0])
    doors = int(argv[1])
    switched2stats = {
        True: [0, 0],
        False: [0, 0],
    }
    for i in range(iterations):
        print('-'*100)
        print("Playing Monty hall ({})".format(i))
        print()
        won, switched = play_monty_hall(doors)
        switched2stats[switched][1] += 1
        if won:
            switched2stats[switched][0] += 1
        print()

    print("="*100)
    print("Let's sum it up!")
    print("\tWhen switched: {}/{} ({} %%)".format(switched2stats[True][0], switched2stats[True][1],
          int(100*switched2stats[True][0]/switched2stats[True][1])))
    print("\tWhen stayed: {}/{} ({} %%)".format(switched2stats[False][0], switched2stats[False][1],
          int(100*switched2stats[False][0]/switched2stats[False][1])))

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
    # main([1000, 3])