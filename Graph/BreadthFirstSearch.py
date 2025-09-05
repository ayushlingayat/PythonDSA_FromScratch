n = 6
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 4), (3, 4)]

# Adjacency list
adjList = [[] for _ in range(n)]
for x, y in edges:
    adjList[x].append(y)
    adjList[y].append(x)

# for i in range(n):
#     print(i, "->", adjList[i])

# Node class for Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def push(self, x):
        newNode = Node(x)
        self.length += 1
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def pop(self):
        if self.front is None:
            return -1
        x = self.front.data
        self.front = self.front.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return x

    def getSize(self):
        return self.length

    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

# BFS
q = Queue()
visited = [False]*n
ans = []

q.push(0)
visited[0] = True
ans.append(0)

while q.getSize() > 0:
    front = q.pop()
    for x in adjList[front]:
        if not visited[x]:
            q.push(x)
            visited[x] = True
            ans.append(x)

print("It's Breadth First Search ", ans)
