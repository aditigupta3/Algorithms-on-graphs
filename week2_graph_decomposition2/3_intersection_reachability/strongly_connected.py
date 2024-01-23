#Uses python3

import sys

sys.setrecursionlimit(200000)

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
    num_scc = 0
    for vertex in order:
        if not visited[vertex]:
            # While exploring vertex, we determine the complete strongly connected component that contains vertex
            do_dfs(vertex)
            num_scc += 1
    return num_scc


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
