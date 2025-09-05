n2 = 5
adjList2 = [
    [1, 3, 4],
    [0, 2],
    [1],
    [0],
    [0]
]

visited = [False] * n2
ans = []


def dfs(i,parent,adjList,visited):
    visited[i] = True

    for x in adjList[i]:
        if x == parent:
            continue
        if visited[x]:
            return True
        if dfs(x,i,adjList,visited):
            return True

    return False

result = dfs(0,-1,adjList2,visited)
print(result)