# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # corner cases
        if head is None or head.next is None:
            return head

        curr = head

        while curr != None and curr.next != None:
            # duplicate aa chuka hee
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
    