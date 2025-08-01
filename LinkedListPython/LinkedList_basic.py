class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.next = c

head = a

print(head.data)           # Output: 5
print(head.next.data)      # Output: 3
print(head.next.next.data) # Output: 7
