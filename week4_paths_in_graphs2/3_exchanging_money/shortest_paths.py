#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    """
    This function uses the bellman ford algorithm to determine the shortest distances between source
    node `s` to all vertices in the graph
    """
    num_vertices = len(adj)

    # Get the list of all edges with their cost
    edges = list()
    for from_node in range(num_vertices):
        for to_node, c in zip(adj[from_node], cost[from_node]):
            edges.append((from_node, to_node, c))

    distance[s] = 0 # Keeping the source node distance as 0
    # Bellman ford algorithm: Relaxing all edges num_vertices times
    for _ in range(num_vertices):
        for edge in edges:
            from_node, to_node, cost = edge
            if distance[from_node] != 10**19 and distance[to_node] > distance[from_node] + cost:
                distance[to_node] = min(distance[to_node], distance[from_node] + cost)

    # If on doing another relaxation, distance to any node changes, there is a cycle from that node
    start_neg = list()
    visited = [False for i in range(num_vertices)]
    for edge in edges:
        from_node, to_node, cost = edge
        if distance[from_node] != 10**19 and distance[from_node] + cost < distance[to_node]:
            start_neg.append(to_node)
            visited[to_node] = True
    
    # Doing a dfs to identify the set of nodes reachable from a negative cycle
    while start_neg:
        neg_node = start_neg.pop()
        for nbr in adj[neg_node]:
            if not visited[nbr]:
                start_neg.append(nbr)
                visited[nbr] = True

    # Modifying the reachable and shortest array
    for vertex in range(num_vertices):
        if distance[vertex] < 10**19:
            reachable[vertex] = 1
        if visited[vertex]:
            shortest[vertex] = 0


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

