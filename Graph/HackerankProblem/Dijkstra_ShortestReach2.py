#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop


#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(n, edges, s):
    # Write your code here
    adjList = [[] for _ in range(n)]  # More Pythonic way to initialize a list of lists

    for edge in edges:
        x = edge[0] - 1
        y = edge[1] - 1
        w = edge[2]

        adjList[x].append([y, w])
        adjList[y].append([x, w])

    heap = []
    dist = [float("inf")] * n

    s -= 1
    dist[s] = 0


    heappush(heap, (dist[s], s))

    while len(heap) > 0:

        d, u = heappop(heap)

        .
        if d > dist[u]:
            continue

        for v, w in adjList[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(heap, (dist[v], v))

    result = []
    for i in range(n):
        if i == s:
            continue
        elif dist[i] == float("inf"):
            result.append(-1)
        else:
            result.append(dist[i])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()