class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # for doubly linked list

# Creating nodes
a = Node(5)
b = Node(3)
c = Node(7)

# Linking nodes
a.next = b
b.prev = a
b.next = c
c.prev = b

head = a

# Print data
print(head.data)           # Output: 5
print(head.next.data)      # Output: 3
print(head.next.next.data) # Output: 7

# Traverse linked list
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

printLinkedList(head)

# Insertion at the beginning
newNode = Node(4)
newNode.next = head
head.prev = newNode
head = newNode

# Insertion at the end
newNode = Node(1)
curr = head
while curr.next is not None:
    curr = curr.next

curr.next = newNode
newNode.prev = curr

# Insertion at kth index
k = 2
newNode = Node(6)
curr = head
for i in range(k - 1):
    curr = curr.next

newNode.next = curr.next
newNode.prev = curr

if curr.next is not None:
    curr.next.prev = newNode
curr.next = newNode

printLinkedList(head)

# Delete the first node
head = head.next
head.prev = None

printLinkedList(head)

# Delete the last node
curr = head
while curr.next.next is not None:
    curr = curr.next

curr.next = None

printLinkedList(head)

# Delete the kth node
k = 2
curr = head
for i in range(k - 1):
    curr = curr.next

toDelete = curr.next
curr.next = toDelete.next
if toDelete.next is not None:
    toDelete.next.prev = curr

printLinkedList(head)
