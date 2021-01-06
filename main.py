"""
Dynamic programming  - Transitive Closure of Directed Graph
"""

def trans_closure(graph):
    """
    Given the adjacency matrix for a directed graph, it computes the reachability
    matrix
    :param graph: adjacency matrix
    :return: reachability matrix
    """
    nodes = len(graph)
    #Copy input graph to a new result graph.
    result = [[graph[i][j] for j in range(nodes)] for i in range(nodes)]

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                result[i][j] = result[i][j] or (result[i][k] and result[k][j])
    return result

#test
graph1 = [[0,1,1,0],
          [0,0,1,0],
          [1,0,0,1],
          [0,0,0,1]]

graph2 = [[1, 1, 0, 1],
          [0, 1, 1, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 1]]

print(trans_closure(graph1))
print(trans_closure(graph2))
