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



# Traverse linked list
def printLinkedList(head):
    curr = head

    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next

printLinkedList(head)

#insertion at the beginning of the linkedlist

newNode = Node(4)
newNode.next = head
head = newNode

# Insertion at the end of the linkedlist
newNode = Node(1)

curr = head
while curr.next != None:
    curr = curr.next

curr.next = newNode

#insertion at the kth index

# Insertion at the kth index
k = 2
newNode = Node(6)

curr = head
for i in range(k - 1):
    curr = curr.next

newNode.next = curr.next
curr.next = newNode

printLinkedList(head)

#Deletion

#Delete the first Node
head = head.next

printLinkedList(head)

# Delete the last node
curr = head
while curr.next.next != None:
    curr = curr.next

curr.next = None

printLinkedList(head)

# Delete the kth node
k = 2

curr = head
for i in range(k - 1):
    curr = curr.next

curr.next = curr.next.next




