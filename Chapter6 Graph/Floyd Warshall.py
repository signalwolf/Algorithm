# coding=utf-8

# 解决的问题：解决图中任意两点之间的最短路径的算法。
# 与Dijkstra的不同：适用于negative的edge的情况（but not negative cycles）
# 基本原型：DP
# 算法： 点A到点B的最短距离是点A到点C后再由C到B的距离之和 与点A到点B距离中更小的那个，C点要遍历所有的node
# Time complexsity: O(N ** 3)

# Input:
#        graph[][] = { {0,   5,  INF, 10},
#                     {INF,  0,  3,  INF},
#                     {INF, INF, 0,   1},
#                     {INF, INF, INF, 0} }
# which represents the following graph
#              10
#        (0)------->(3)
#         |         /|\
#       5 |          |
#         |          | 1
#        \|/         |
#        (1)------->(2)
#             3
# Note that the value of graph[i][j] is 0 if i is equal to j
# And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.
#
# Output:
# Shortest distance matrix
#       0      5      8      9
#     INF      0      3      4
#     INF    INF      0      1
#     INF    INF    INF      0

V = 4
INF = float('inf')
# Solves all pair shortest path via Floyd Warshall Algorithm
def floydWarshall(graph):
    """ dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix 
    OR we can say that the initial values of shortest distances 
    are based on shortest paths considering no  
    intermediate vertices """
    dist = map(lambda i: map(lambda j: j, i), graph)

    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)

# A utility function to print the solution
def printSolution(dist):
    print "Following matrix shows the shortest distances between every pair of vertices"
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print "%7s" % ("INF"),
            else:
                print "%7d\t" % (dist[i][j]),
            if j == V - 1:
                print ""



# Driver program to test the above program
# Let us create the following weighted graph
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
# Print the solution
printSolution(graph)
floydWarshall(graph);