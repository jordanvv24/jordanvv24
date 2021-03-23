from math import inf
import copy
from Lab3.graphs import adjacency_list


def distance_matrix(adj_list):
    n = len(adj_list)
    distance = [[inf for _ in range(n)] for _ in range(n)]  # Initialises an nxn matrix of inf

    for i in range(n):
        distance[i][i] = 0      # make the diagonal all zeros

    for i in range(n):      # step through each line in the adj list
        for edge in adj_list[i]:        # step through each edge in the line
            destination, weight = edge
            distance[i][destination] = weight

    return distance


def floyd(distance):
    """"Takes an adjacency list and returns a matrix containing the shortest
    distance from any vertex to any other vertex.
    """
    n = len(distance)
    shortest_dist = copy.deepcopy(distance)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if shortest_dist[i][j] > shortest_dist[i][k] + shortest_dist[k][j]:
                    shortest_dist[i][j] = shortest_dist[i][k] + shortest_dist[k][j]

    return shortest_dist
