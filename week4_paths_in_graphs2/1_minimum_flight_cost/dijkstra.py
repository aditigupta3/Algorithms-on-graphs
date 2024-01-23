#Uses python3

import sys
from heapq import heappush, heappop


def distance(adj, cost, s, t):
    """
    This function uses the Dijkstra's algorithm to find the shortest between source, `s` and target, `t`
    in a graph defined using adjacency list `adj` with weights on the graph edges defined using `cost`
    """
    heap = [(0, s)]
    visited = [False for i in range(len(adj))]
    while heap:
        total_dis, next_node = heappop(heap)
        if not visited[next_node]:
            if next_node == t:
                return total_dis
            visited[next_node] = True
            for nbr_, cost_ in zip(adj[next_node], cost[next_node]):
                if not visited[nbr_]:
                    heappush(heap, (total_dis + cost_, nbr_))
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
