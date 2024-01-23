#Uses python3

import sys

def toposort(adj):
    """
    Given the adjacency list reprsentation of a directed graph - adj,
    determine the topological sorting for it.
    """
    # order contains the vertices in the postorder order
    # the vertex that will be first will be one that is done exploring first and so on.
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
    # The topological sort is in the reverse postorder
    return list(reversed(order))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

