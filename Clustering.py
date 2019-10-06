# Clustering

import random
import matplotlib.pyplot as plt


class Space:
    def __init__(self, nb_points):
        self.nb = nb_points
        self.points = list()
        for i in range(nb_points):
            self.points.append([random.randint(-20, 20), random.randint(-20, 20)])

    def afficher(self):
        x = []
        y = []
        for i in range(self.nb):
            x.append(self.points[i][0])
            y.append(self.points[i][1])
        plt.scatter(x, y)
        plt.axis(xlim=(-20, 20), ylim=(-20, 20))
        plt.legend("Space with points")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
