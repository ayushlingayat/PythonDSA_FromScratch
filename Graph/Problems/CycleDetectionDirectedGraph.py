n2 = 5
adjList2 = [
    [1, 2],   # 0 -> 1,2
    [2],      # 1 -> 2
    [3],      # 2 -> 3
    [1],      # 3 -> 1 (back edge, cycle)
    []        # 4 -> no edges
]

visited = [False] * n2
dfsVisited = [False] * n2

def dfs(i, adjList, visited, dfsVisited):
    visited[i] = True
    dfsVisited[i] = True  # mark in current recursion path

    for x in adjList[i]:
        if not visited[x]:
            if dfs(x, adjList, visited, dfsVisited):
                return True
        elif dfsVisited[x]:   # if node is already in current path → cycle
            return True

    dfsVisited[i] = False  # backtrack
    return False

def isCyclic(n, adjList):
    visited = [False] * n
    dfsVisited = [False] * n

    for i in range(n):
        if not visited[i]:
            if dfs(i, adjList, visited, dfsVisited):
                return True
    return False

print("Cycle exists?", isCyclic(n2, adjList2))
