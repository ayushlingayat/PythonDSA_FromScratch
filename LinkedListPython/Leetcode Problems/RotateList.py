# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        # Step 1: Calculate length and get last node
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1

        # Step 2: Effective rotation
        k = k % length
        if k == 0:
            return head

        # Step 3: Find new tail
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        # Step 4: Rotate
        new_head = curr.next
        curr.next = None
        last.next = head

        return new_head
