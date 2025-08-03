class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

# Test code
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop())      # 5
print(stack.getTop())   # 4
print(stack.size())     # 4
