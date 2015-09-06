__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy as sp
import random
import time

# ---------------------------------------------------------------
# Class - Graph
# ---------------------------------------------------------------


class WalkableGraph:
    """Graph on which we can do random walking"""
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, file_path):
        """ Loads a graph from file

        The file should have format:
        CityName i_1 i_2 ... i_k
        ....

        where i_j are indices of neighbouring cities (index given by index of the row)
        """
        self._graph = []
        self._cities = []
        with open(file_path, 'r') as f:
            for line in f:
                city = line.split(' ')[0]
                neighs = [int(s) for s in line.split(' ')[1:]]
                self._cities.append(city)
                self._graph.append(neighs)
        self.n = len(self._cities)
        self._current_city_index = None
        self._transition_matrix = self.__get_transition_matrix()

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def print(self):
        """ Prints the neighbourhood table of the graph """
        for i in range(self.n):
            print(str(i) + " " + self._cities[i] + " " + str(len(self._graph[i])) + " " + str(self._graph[i]))

    def probs_after_k_steps(self, k):
        """ Prints the probability (for each city) we end up in the city after k steps """
        probs = (1/self.n)*sp.ones(self.n)
        for i in range(k):
            probs = sp.dot(self._transition_matrix, probs)

        print("Probabilities: ")
        for i in range(self.n):
            print("\t" + self._cities[i] + ": " + str(probs[i]))

        return probs

    def random_walk(self, start_city, steps=10, time_in_city=0):
        """ Does a random walk through the graph, starting at given city, making "steps" random steps and waiting in
        each city for time_in_city seconds
        """
        self.start_walking(start_city)
        print("Random walk with " + str(steps) + " steps. Started in " + self.get_current_city())
        visits = [0]*self.n
        for i in range(steps):
            visits[self._current_city_index] += 1
            self.walk_to_next()
            time.sleep(time_in_city)
        visits[self._current_city_index] += 1
        print("Finished random walk in: " + self.get_current_city())
        print("Visits of cities: ")
        for i in range(self.n):
            print("\t%s: %s (%s)" % (self._cities[i], visits[i], visits[i]/steps))

    def start_walking(self, start_city):
        """ Starts the random walking in a given city """
        self._current_city_index = None
        for i in range(len(self._cities)):
            if self._cities[i] == start_city:
                self._current_city_index = i
        if self._current_city_index is None:
            raise Exception("Unknown city " + start_city)
        print("Started walking in " + self.get_current_city())

    def get_current_city(self):
        """ Gets the current city on the random walk """
        if self._current_city_index is None:
            raise Exception("We did not start walking")
        return self._cities[self._current_city_index]

    def walk_to_next(self):
        """ Moves to a random neighbour of the current city """
        if self._current_city_index is None:
            raise Exception("We did not start walking")
        neigh_count = len(self._graph[self._current_city_index])
        neigh_index = random.randint(0, neigh_count - 1)
        # random.choice(self._graph[self._current_city_index])
        self._current_city_index = self._graph[self._current_city_index][neigh_index]

        print("Moved to " + self.get_current_city())

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __get_transition_matrix(self):
        """ Gets the transition matrix of the graph """
        transition_matrix = sp.zeros((self.n, self.n))
        for j in range(self.n):
            for i in self._graph[j]:
                transition_matrix[i][j] = 1/len(self._graph[j])

        return transition_matrix

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    random.seed()
    g = WalkableGraph('ghana.txt')
    g.print()
    # g.start_walking("Accra")
    # g.walk_to_next()
    # g.walk_to_next()
    # print("I am in this city: " + g.get_current_city())
    #
    # print()
    # print("Let's do some walking")
    k = 10
    g.random_walk("CapeCoast", k, 0)
    # g.probs_after_k_steps(k)

if __name__ == '__main__':
    main()
