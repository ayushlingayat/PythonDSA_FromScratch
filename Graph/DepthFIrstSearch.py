class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
n = 6
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

# Adjacency list
adjList = [[] for _ in range(n)]
for x, y in edges:
    adjList[x].append(y)
    adjList[y].append(x)

# for i in range(n):
#     print(i, "->", adjList[i])


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x):
        self.length += 1
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            return -1
        self.length -= 1
        x = self.top.data
        self.top = self.top.next
        return x

    def getTop(self):
        if self.top is None:
            return -1
        return self.top.data

    def size(self):
        return self.length

st = Stack()
visited = [False]*n
ans = []

st.push(0)
visited[0] = True


while st.size() > 0:
    top = st.pop()
    ans.append(top)
    for x in adjList[top]:
        if not visited[x]:
            st.push(x)
            visited[x] = True

print("It's Depth First Search ", ans)
