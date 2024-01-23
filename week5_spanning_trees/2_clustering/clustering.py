#Uses python3
import sys
import math

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

def clustering(x, y, k):
    """
    Given points on a plane with coordinates defined using x and y and an integer k,
    this function computes the largest possible value of d such that the given points can be partitioned into
    k non-empty subsets in such a way that the distance between any two points from different subsets is at least d.
    """
    num_pts = len(x)
    # Computing the distances between all pairs of points
    dist = list()
    for i, pt1 in enumerate(zip(x, y)):
        for j, pt2 in enumerate(zip(x, y)):
            if j > i:
                dist.append((get_distance(pt1, pt2), i, j))

    dist.sort()
    # If we do `num_merges` merges, we end up with k clusters.
    # The very next distance will be the required answer.
    num_merges = num_pts - k
    set_ = DisjointSet(num_pts)
    idx = 0
    while num_merges > 0 and idx < len(dist):
        # If the points don't already belong to the same set, connect them
        _, first_, second_ = dist[idx]
        set_.union(first_, second_)
        num_merges -= 1
        while set_.find(dist[idx][1]) == set_.find(dist[idx][2]):
            idx += 1
            if idx == len(dist):
                break
    if idx == len(dist):
        return -1
    else:
        return dist[idx][0]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
