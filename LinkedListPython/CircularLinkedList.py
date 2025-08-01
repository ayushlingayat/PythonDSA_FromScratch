class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
a = Node(10)
b = Node(20)
c = Node(30)

# Linking nodes in circular manner
a.next = b
b.next = c
c.next = a  # circular link

# Set head
head = a

# Traverse circular linked list
curr = head
while True:
    print(curr.data, end=" ")
    curr = curr.next
    if curr == head:
        break

