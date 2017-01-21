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
        # find the index of the start-city
        current_city_index = None
        for i in range(len(self._cities)):
            if self._cities[i] == start_city:
                current_city_index = i
        if current_city_index is None:
            raise Exception("Unknown city " + start_city)

        # do the random walking
        print("Random walk with " + str(steps) + " steps. Started in " + self._cities[current_city_index])
        visits = [0]*self.n
        for i in range(steps):
            visits[current_city_index] += 1
            current_city_index = random.choice(self._graph[current_city_index])
            print("Moved to " + self._cities[current_city_index])
            time.sleep(time_in_city)
        visits[current_city_index] += 1

        # print the statistics
        print("Finished random walk in: " + self._cities[current_city_index])
        print("Visits of cities: ")
        for i in range(self.n):
            print("\t%s: %s (%s)" % (self._cities[i], visits[i], visits[i]/steps))

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

    print()
    print("Let's do some walking")
    k = 1000
    g.random_walk("CapeCoast", k, 0)
    # g.probs_after_k_steps(k)

if __name__ == '__main__':
    main()
