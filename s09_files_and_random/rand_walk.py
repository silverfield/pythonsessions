import random
import time

class WalkableGraph:
    def __init__(self, file_name):
        self._graph = []
        self._towns = []
        with open(file_name, 'r') as f:
            for line in f:
                town = line.split(' ')[0]
                neighs = line.split(' ')[1]
                self._graph.append([int(i) for i in neighs.split(',')])
                self._towns.append(town)

    def print(self):
        for i in range(len(self._towns)):
            print(str(i) + " " + self._towns[i] + " " + str(self._graph[i]))

    def random_walk(self, start_city_index, k, t):
        current_index = start_city_index

        visits = [0]*len(self._towns)
        for i in range(k):
            visits[current_index] += 1
            print("We are in " + self._towns[current_index])
            time.sleep(t)
            current_index = random.choice(self._graph[current_index])
        visits[current_index] += 1

        print("We ended up in " + self._towns[current_index])
        for i in range(len(self._towns)):
            print("\t" + self._towns[i] + ": " + str(visits[i]) + " " + str(visits[i]/k))

random.seed()
g = WalkableGraph("gh.txt")
g.print()
g.random_walk(1, 100000, 0)