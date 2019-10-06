import numpy as np


def distance(point1, point2):
    return np.sqrt((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)


def nn_solver(i, j, points):
    if i == j:
        return "i == j"
    liste1 = [points[i]]
    liste2 = [points[j]]
    for k in range(len(points)):
        if i == k or j == k:
            continue
        if distance(points[i], points[k]) < distance(points[j], points[k]):
            liste1.append(points[k])
        else:
            liste2.append(points[k])
    return [liste1, liste2]
