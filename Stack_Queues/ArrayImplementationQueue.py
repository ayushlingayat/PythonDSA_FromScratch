# List implementation of Queue
class Queue:
    def __init__(self):
        self.q = []
        self.front = 0

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if self.front >= len(self.q):
            return -1
        x = self.q[self.front]
        self.front += 1
        return x

    def getFront(self):
        if self.front >= len(self.q):
            return -1
        return self.q[self.front]

    def size(self):
        return len(self.q) - self.front

# Test code
queue = Queue()
queue.push(5)
queue.push(4)
queue.push(3)
queue.push(1)

print(queue.pop())      # 5
print(queue.getFront()) # 4
print(queue.size())     # 3
