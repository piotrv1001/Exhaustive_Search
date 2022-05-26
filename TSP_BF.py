from sys import maxsize
from itertools import permutations
 
def TSP_BF(graph, s, V):

    vertices = []
    for i in range(V):
        if i != s:
            vertices.append(i)
 
    min_path = maxsize
    next_permutation = permutations(vertices)

    smallest_tuple = None

    for i in next_permutation:
 
        current_pathweight = 0
 
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # min_path = min(min_path, current_pathweight)
        if current_pathweight < min_path:
            smallest_tuple = i
            min_path = current_pathweight
         
    return (min_path, smallest_tuple)


def printShortestPath(smallest_tuple, source):

    li = list(smallest_tuple)
    li.append(source)
    li2 = [source]
    li2.extend(li)
    li2 = [x + 1 for x in li2]
    string = ",".join(str(x) for x in li2)

    return string