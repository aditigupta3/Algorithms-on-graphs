#Uses python3

import sys


def acyclic(adj):
    """
    This function checks if the given directed graph contains any cycles.
    """
    def do_dfs(vertex):
        """
        This function returns whether or not a cycle was found while exploring vertex in graph adj
        """
        # Mark the node as visited and add it to the recursion stack
        visited[vertex] = True
        recStack[vertex] = True
        for nbr in adj[vertex]:
            # explore all unvisited neighbours - If a cycle is found while exploring them, return cycle found
            if not visited[nbr]:
                if do_dfs(nbr):
                    return True
            # If any neighbour is visited and present in the recursion stack, there is a cycle
            elif recStack[nbr]:
                return True
        # Remove the vertex from recursion stack
        recStack[vertex] = False
        return False
    num_vertices = len(adj)
    visited = [False for i in range(num_vertices)]
    recStack = [False for i in range(num_vertices)]
    for vertex in range(len(adj)):
        if not visited[vertex]:
            if do_dfs(vertex):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
