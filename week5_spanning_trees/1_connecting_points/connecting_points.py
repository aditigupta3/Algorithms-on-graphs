#Uses python3
import sys
import math
from collections import defaultdict

class DisjointSet():
    def __init__(self, num_pts):
        self.parent = [i for i in range(num_pts)]
        self.rank = [1 for i in range(num_pts)]
    def find(self, i):
        while i!=self.parent[i]:
            i = self.parent[i]
        return i
    def union(self, i, j):
        parenti = self.find(i)
        parentj = self.find(j)
        # Using union by rank heuristic
        if self.rank[parenti] > self.rank[parentj]:
            self.parent[parentj] = parenti
        elif self.rank[parenti] < self.rank[parentj]:
            self.parent[parenti] = parentj
        else:
            self.parent[parentj] = parenti
            self.rank[parenti] += 1

def get_distance(pt1, pt2):
    return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

def minimum_distance(x, y):
    """
    Given the x and y coordinates of a set of points, this function calculates the minimum length
    of string required to connect all of them - the distance of the minimum spanning tree.
    """
    num_pts = len(x)
    # Computing the distances between all pairs of points
    dist = list()
    for i, pt1 in enumerate(zip(x, y)):
        for j, pt2 in enumerate(zip(x, y)):
            if i!=j:
                dist.append((get_distance(pt1, pt2), i, j))
    result = 0.
    # Using Kruskals Algorithm to find the minimum spanning tree
    set_ = DisjointSet(num_pts)
    for distance, i, j in sorted(dist):
        # If the points don't already belong to the same set, connect them
        if set_.find(i) != set_.find(j):
            set_.union(i, j)
            result += distance
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
