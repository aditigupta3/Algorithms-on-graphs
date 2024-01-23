#Uses python3

import sys


def number_of_components(adj):
    """
    This function determines the number of connected components in the graph
    """
    result = 0
    num_vertices = len(adj)
    # Initially all vertices are not visited
    visited = [False for i in range(num_vertices)]
    for i in range(num_vertices):
        if not visited[i]:
            # Do DFS starting from vertex i
            result += 1
            visited[i] = True
            dfs_stack = [i]
            while dfs_stack:
                elem = dfs_stack.pop()
                for nbr in adj[elem]:
                    if not visited[nbr]:
                        dfs_stack.append(nbr)
                        visited[nbr] = True
    return result

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
    print(number_of_components(adj))
