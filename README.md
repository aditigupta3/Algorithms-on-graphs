
# Algorithms on Graphs
My solution for the "Algorithms on Graphs" course on Coursera:
https://www.coursera.org/learn/algorithms-on-graphs/

Here are my notes from the specialisation:

## Graphs
* Simple graphs: Have no loops and no multiple edges between 2 vertices.
* Representing graphs: Different operations are faster in different representations.
    * List of edges
    * Adjacency matrix
    * Adjacency list: Good for many problems.
* Exploring undirected graphs:
    * Keep a track of visited nodes.
    * Depth first ordering: call explore recursively unless we reach a node that doesn't have any neighbour or has already been visited. Time: $O(|V|+|E|)$
    * Connected components without any edges between them can be found using DFS.
    * Previsit and postvisit orderings can be useful for some algorithms.

## Directed Graphs
* Directed Acyclic Graph (DAG): A directed graph with no cycles
* Linear ordering:
    * If the graph contains a cycle, it can't be linearly ordered. Also, any DAG can be linearly ordered.
    * Topological sort:
        * do DFS(G)
        * sort the vertices by reverse post order
* Connectivity in directed graphs:
    * Strongly connected components: Any two vertices are reachable from each other.
    * A directed graph can be partitioned into SCCs where 2 vertices are connected if and only if they are in the same component.
    * Metagraph - How these SCCs connect to each other - will always be a DAG.
    *  To compute SCCs. Runtime: $O(|V|+|E|)$:
    ```
    def SCCs(G):
        run DFS(G_R) # where G_R is the reverse graph
        for v in reverse post order:
            if not visited(v):
                run Explore(v)
                mark visited vertices as new SCC
    ```

## Shortest Path Algorithms
* **Breadth First Search:**
    * Time complexity : $O(|V|+|E|)$ since each vertex is enqueued at most once and each edge is examined at most once.
    * In order to reconstruct the shortest path, the previous node to a node can be saved.
    * BFS uses queues, DFS uses stacks.
* **Naive algorithm:**
    * Start with infinite distances for all nodes except source (for which the distance value is 0)
    * Until some distance value changes - For each vertex, keep on relaxing every edge. <br> Edge relaxation means: 
```
if dist[v] > dist[u] + w(u, v):
    dist[v] = dist[u] + w(u, v)
    prev[v] = u
```
* **Dijstra's Algorithm:** Optimised algorithm for graphs with no negative edge weights.
    * Uses priority queues instead of queues - Maintain a heap for the neighbouring nodes and pick the one with the minimum distance to relax edges from.
    * Useful operations: MakeQueue, ExtractMin, ChangePriority (not present in the heapq implementation in Python).
    * Total time has components:
        * $O(V)$, time required to initialise distance values
        * $T(MakeQueue)$, time required to construct the heap
        * $|V|*T(ExtractMin)$, time required to extract the closest node
        * $|E|*T(ChangePriority)$, time required for edge relaxations
    * Best implementation depends on the structure of the graph: 
        * If implemented as an array time is $O(|V|^2)$
        * If implemented as a binary heap time is $O((|V| + |E|)*log(|V|))$
* **Bellman Ford Algorithm:** Can be applied to graphs with negative weights as well - useful for applications like currency arbitrage.
    * Negative weight cycles: Because of these, the distance between two nodes can be $-\inf$. Bellman ford algorithm doesn't work in this case.
    * Can use naive algorithm using edge relaxations - instead of running every edge relaxation until some dist value changes, repeat edge relaxations $|V|-1$ times.
    * Running time: $O(|V||E|)$
    * In order to detect these negative weight cycles:
        * run the edge relaxations once again.
        * If the distance of any vertex v changes, v is reachable from a negative weight cycle.
        * Starting from v, follow the prev[v] for $|V|$ times - this will definitely be on the cycle.


## Minimum Spanning Trees
A subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together without any cycles and with the minimum possible total edge weight.
* A tree is an undirected graph that is connected and acyclic.
* A tree with $n$ vertices has $n-1$ edges.
* **Kruskal's Algorithm:** Repeatedly add lightest edge if this doesn't produce a cycle.
    * At any point of time, the set of edges, X in MST is a collection of trees.
    * Thus, this uses disjoint sets data structure.
    * Running time:
        * Sorting edges: $O(|E|log(|E|)) \lt O(|E|log(|V|^2)) = O(|E|log(|V|))$
        * Processing edges: $2*|E|*T(Find) + |V|T(Union) = O(|E|log(|V|))$

* **Prim's Algorithm:** Start with any vertex as a root and repeatedly attach a new vertex to the current tree by a lightest edge.
    * Priority Queue data structure - very similar to the Dijkstra's algorithm.
    * Running Time: Similar to Dijkstra's algorithm: $|V|*T(ExtractMin) + |E|*T(ChangePriority)$
    * Best implementation depends on the structure of the graph: 
        * If implemented as an array time is $O(|V|^2)$
        * If implemented as a binary heap time is $O((|V| + |E|)*log(|V|))$


## Advanced shortest paths Algorithms
For non negative edge weight graphs, in order to find the shortest path between source, $s$ and target, $t$.
* For undirected graphs Mikkel Thorup came up with a linear time algorithm.
* **Bidirectional Dijkstra's:**
    * Suppose each vertex has outvalency about $m$, and the edge distance from $s$ to $t$ is $n$. Then, in case of unidirectional Dijkstra's we expect to relax $O(m^n)$ edges, while for bidirectional Dijkstra's, we would only relax $O(m^{n/2})$ edges. 2* speedup for road network, 1000* faster for social networks.
    * How to combine the search from source, $s$ and target, $t$? The shortest path doesn't necessarily pass through the meeting point, but has been processed either in the forward search or the reverse search.

* __A* Algorithm:__
    * A **directed search** algorithm using a heuristic - potential function. Done by redefining edge weights:
    $w_\pi(u, v) = w(u, v) - \pi(u)+\pi(v)$
    * This doesn't change the shortest path. Use Dijksta's with potentials.
    * How to choose potential function?
        * The edge weights must be non negative after transformation.
        * $\pi(v)$ gives a lower bound on the distance from $v$ to target, $t$. Best case - when exactly equal.
    * Bidirectional A* Algorithm:
        * Same as bi directional Dijkstra's but with potentials.
        * Needs 2 potentials - one for forward search and the other for reverse. Problem - they will lead to 2 different edge weights.
        <br>
        $w_{\pi f}(u, v) = w(u, v) - \pi_f(u)+\pi_f(v)$
        <br>
        $w_{\pi r}(u, v) = w(u, v) - \pi_r(u)+\pi_r(v)$
        * $w_{\pi f}(u, v) = w_{\pi r}(u, v) => \pi_f(u) + \pi_r(u) = \pi_f(v) + \pi_r(v)$ for any $(u,v)$.
        * Use $p_f(u)= \frac {(\pi_f(u) - \pi_r(u))} 2, p_r(u) = -p_f(u)$
    * Landmarks: Fix some vertex $A \in V$ we call it a landmark. Then potential $\pi(v) = d(A, t) - d(A, v)$ is feasible, and $\pi(t) = 0$. 
        * We keep precomputed distances from the landmark to all vertices in the graph. This increases the space complexity and precompute cost, but significantly speeds up the search.
        * Good Landmarks are usually around the boundary of the map
* **Contraction Hierarchies:**
    * Important ideas:
        * long distance trips usually go through highways.
        * Nodes can be ordered by some importance factor => highways are much more important than small streets. For any specific shortest route, the importance first increases and then decreases back along any shortest path.
        * Many shortest paths involve important nodes.
        * Important nodes are spread around
        * Important nodes are sometimes unavoidable.
    * Shortest paths with preprocessing:
        * Preprocess the graph
        * Find distance and shortest path in the preprocessed graph
        * Reconstruct the shortest path in the initial graph.
    * Preprocessing
        * Node contraction: When a node is contracted, any shortest path that goes through it - add a new edge corresponding to that in the graph - this created the augmented graph.
        * When contracting a new edge $v$, for every pair of edges $(u, v), (v, w)$ if there is a shortest path through v, add a new edge $(u, w)$ with $l(u, w) = l(u, v) + l(v, w)$
- REMAINING PENDING
