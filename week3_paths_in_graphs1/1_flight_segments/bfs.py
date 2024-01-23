#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    """
    Given the graph representation of an undirected graph - adj,
    this function finds the shortest path between source - s and target - t.
    The function uses breadth first search using a double ended queue - deque.
    """
    to_check = deque([(s, 0)])
    visited = [False for i in range(len(adj))]
    visited[s] = True
    while to_check:
        node, num_jumps = to_check.popleft()
        if node == t:
            return num_jumps
        for nbr in adj[node]:
            if not visited[nbr]:
                to_check.append((nbr, num_jumps+1))
                visited[nbr] = True
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
