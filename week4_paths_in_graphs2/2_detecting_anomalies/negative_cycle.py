#Uses python3

import sys

def toposort(adj):
    """
    Function for topological sorting
    """
    order = []
    num_vertices = len(adj)
    visited = [False for i in range(num_vertices)]
    def do_dfs(vertex):
        visited[vertex] = True
        for nbr in adj[vertex]:
            if not visited[nbr]:
                do_dfs(nbr)
        order.append(vertex)
    for i in range(num_vertices):
        if not visited[i]:
            do_dfs(i)
    return list(reversed(order))

def number_of_strongly_connected_components(adj):
    """
    Given the directed graph adj, determine the number of strongly connected components in the graph
    """
    def do_dfs(vertex):
        visited[vertex] = True
        for nbr in adj[vertex]:
            if not visited[nbr]:
                do_dfs(nbr)

    # Determine the reverse graph
    num_vertices = len(adj)
    adjR = [list() for i in range(num_vertices)]
    for i in range(num_vertices):
        for j in adj[i]:
            adjR[j].append(i)
    # Get topological sorting for the reverse graph
    order = toposort(adjR)

    visited = [False for i in range(num_vertices)]
    scc = list()
    for vertex in order:
        if not visited[vertex]:
            # While exploring vertex, we determine the complete strongly connected component that contains vertex
            do_dfs(vertex)
            scc.append(vertex)
    return scc

def negative_cycle(adj, cost):
    """
    Given the graph `adj` with edge weights `cost`,
    the function determines whether there is a negative weight cycle in the graph.
    This assumes that the graph is a connected graph.
    """
    num_vertices = len(adj)

    # Get the list of all edges with their cost
    edges = list()
    for from_node in range(num_vertices):
        for to_node, c in zip(adj[from_node], cost[from_node]):
            edges.append((from_node, to_node, c))

    # For each strongly connected component, mark 1 vertex as the start point
    distances = [float('inf') for i in range(num_vertices)]
    for vertex in number_of_strongly_connected_components(adj):
        distances[vertex] = 0 # Keeping the first node as the start point

    # Relaxing all edges num_vertices times
    for _ in range(num_vertices):
        for edge in edges:
            from_node, to_node, cost = edge
            distances[to_node] = min(distances[to_node], distances[from_node] + cost)

    # If on doing another relaxation, any distance changes, the graph has a cycle
    for edge in edges:
        from_node, to_node, cost = edge
        if distances[from_node] + cost < distances[to_node]:
            return 1
    return 0


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
    print(negative_cycle(adj, cost))
