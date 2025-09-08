from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def push(self, x):
        newNode = Node(x)
        self.length += 1
        if self.front is None:
            self.front = newNode
            self.rear = newNode
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


class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        q = Queue()
        ans = []
        indegree = [0] * n
        adjList = [[] for _ in range(n)]

        for a, b in prerequisites:
            indegree[a] += 1
            adjList[b].append(a)

        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
                q.push(i)

        while q.getSize() > 0:
            front = q.pop()
            for x in adjList[front]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    ans.append(x)
                    q.push(x)

        return len(ans) == n
