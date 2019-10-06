from Clustering import Space
from DumbNeareastNeighbor import nn_solver
import random
import matplotlib.pyplot as plt

nb_points = 5

space = Space(nb_points)
i, j = random.sample([0, nb_points-1], 2)
cluster = nn_solver(i, j, space.points)


def afficher_cluster(points1, points2):
    listepoints = [points1, points2]
    listcolors = ['red', 'blue']
    for i in range(2):
        x = []
        y = []
        for j in range(len(listepoints[i])):
            x.append(listepoints[i][j][0])
            y.append(listepoints[i][j][1])
        plt.scatter(x, y, c=listcolors[i])
    plt.axis(xlim=(-20, 20), ylim=(-20, 20))
    plt.legend("binary Cluster")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


afficher_cluster(cluster[0], cluster[1])
