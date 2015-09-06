__author__ = 'ferrard'

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

import scipy
import math
from pyx import canvas
from pyx import path
from pyx import deco

# ---------------------------------------------------------------
# Class - graph
# ---------------------------------------------------------------


class Graph:
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            self.n = int(lines[0])
            self.adj_mat = scipy.zeros((self.n, self.n))
            self.adj_mat.fill(None)
            for line in lines[1:]:
                x = int(line.split(' ')[0])
                y = int(line.split(' ')[1])
                weight = int(line.split(' ')[2])
                self.adj_mat[x, y] = weight

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def draw(self, r=5):
        c = canvas.canvas()

        x_centre = r + 1
        y_centre = r + 1

        angle_diff = 2*math.pi/self.n

        def get_pos(index):
            x_pos = x_centre + math.sin(index*angle_diff)*r
            y_pos = y_centre + math.cos(index*angle_diff)*r
            return x_pos, y_pos

        # nodes
        for i in range(self.n):
            x, y = get_pos(i)
            c.stroke(path.circle(x, y, 1))
            c.text(x, y, i)

        # edges
        for i in range(self.n):
            for j in range(self.n):
                if math.isnan(self.adj_mat[i, j]):
                    continue
                x1, y1 = get_pos(i)
                x2, y2 = get_pos(j)
                x_offset = (x2 - x1)/math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                y_offset = (y2 - y1)/math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                arc = path.line(x1 + x_offset, y1 + y_offset, x2 - x_offset, y2 - y_offset)
                c.stroke(arc, [deco.earrow()])
                c.text((x1 + x2)/2 + x_offset, (y1 + y2)/2 + y_offset, self.adj_mat[i, j])  # moved towards the end pt

        c.writePDFfile("graph")

    def set_edge(self, x, y, weight):
        if weight < 0:
            raise ValueError("Weight must be positive")

        self.adj_mat[x, y] = weight

    def rem_edge(self, x, y):
        self.adj_mat[x, y] = None

    def is_connected(self):
        visited = [False] * self.n
        to_visit = [0]

        while len(to_visit) > 0:
            current = int(to_visit.pop())
            if visited[current]:
                continue

            to_visit.extend(self.__neighbours(current))
            visited[current] = True

        if all(v for v in visited):
            return True
        return False

    def are_connected(self, x, y):
        visited = [False] * self.n
        to_visit = [x]

        while len(to_visit) > 0:
            current = int(to_visit.pop())
            if current == y:
                return True
            if visited[current]:
                continue

            to_visit.extend(self.__neighbours(current))
            visited[current] = True

        return False

    def shortest_path(self, x, y):
        pass

    def print_adj_matrix(self):
        print(self.adj_mat)

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __neighbours(self, x):
        for y in range(self.n):
            if not math.isnan(self.adj_mat[x, y]):
                yield y

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------


def main():
    g = Graph('/home/ferrard/workspace/aims/code/s06_classes_intro/solutions/gr.txt')
    g.print_adj_matrix()
    print("Is connected: " + str(g.is_connected()))
    print("Are 0 and 4 connected: " + str(g.are_connected(0, 4)))
    print("Are 4 and 0 connected: " + str(g.are_connected(4, 0)))
    print("Are 0 and 1 connected: " + str(g.are_connected(0, 1)))
    g.draw()

if __name__ == "__main__":
    main()