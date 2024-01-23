#Uses python3

import sys

def reach(adj, x, y):
    """
    This function determines if node y is reachable from x in graph defined by adj.
    """
    # If the start and end positions are the same, return True
    if x == y:
        return True
    num_vertices = len(adj)
    # Initially all vertices are not visited
    visited = [False for i in range(num_vertices)]
    dfs_stack = [x]
    while dfs_stack:
        elem = dfs_stack.pop()
        # Explore all neighbours of the last node
        for nbr in adj[elem]:
            if not visited[nbr]:
                if nbr == y:
                    return 1
                dfs_stack.append(nbr)
                visited[nbr] = True
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
