# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Deque using Doubly Linked List
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def pushFront(self, x):
        newNode = Node(x)
        self.length += 1
        if self.front is None:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode

    def pushRear(self, x):
        newNode = Node(x)
        self.length += 1
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

    def popFront(self):
        if self.front is None:
            return -1
        x = self.front.data
        self.front = self.front.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return x

    def popRear(self):
        if self.rear is None:
            return -1
        x = self.rear.data
        self.rear = self.rear.prev
        self.length -= 1
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return x

    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

    def getRear(self):
        if self.rear is None:
            return -1
        return self.rear.data

    def getSize(self):
        return self.length

# Test code
deque = Deque()
deque.pushRear(10)
deque.pushFront(20)
deque.pushRear(30)
deque.pushFront(40)

print(deque.popFront())   # 40
print(deque.popRear())    # 30
print(deque.getFront())   # 20
print(deque.getRear())    # 10
print(deque.getSize())    # 2
