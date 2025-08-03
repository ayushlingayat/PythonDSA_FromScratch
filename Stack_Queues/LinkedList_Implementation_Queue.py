# Linked List Implementation of Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0  # fixed typo from 'lenght'

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

    def getFront(self):  # fixed typo from 'greatFront'
        if self.front is None:
            return -1
        return self.front.data

# Test code (placed outside class)
queue = Queue()
queue.push(5)
queue.push(4)
queue.push(3)
queue.push(1)

print(queue.pop())        # 5
print(queue.getFront())   # 4
print(queue.getSize())    # 3
