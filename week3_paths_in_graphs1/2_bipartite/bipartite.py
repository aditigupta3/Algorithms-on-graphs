#Uses python3

import sys
from collections import deque

def bipartite(adj):
    """
    Given the graph representation of an undirected graph - adj,
    this function determines if it is bipartite
    """
    visited = [-1 for i in range(len(adj))]
    for s in range(len(adj)):
        if visited[s] == -1:
            # For each connected component of the graph, we pick the first node and colour it 0
            to_visit = deque([(s, 0)])
            visited[s] = 0
            while to_visit:
                node, val = to_visit.popleft()
                for nbr in adj[node]:
                    if visited[nbr] == val:
                        # If the color of the neighbour is the same, the graph is not bipartite
                        return 0
                    elif visited[nbr] == -1:
                        # We give all neighbours the opposite color
                        otherval = int(not bool(val))
                        to_visit.append((nbr, otherval))
                        visited[nbr] = otherval
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
