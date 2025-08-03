class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]

    def size(self):
        return len(self.st)

    def __str__(self):
        return f"Stack (top -> bottom): {list(reversed(self.st))}"

# Test code
stack = Stack()

stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

print(stack)
print(stack.pop())
print(stack.top())
print(stack.size())

# push - O(1)
# pop - O(1)
# top - O(1)