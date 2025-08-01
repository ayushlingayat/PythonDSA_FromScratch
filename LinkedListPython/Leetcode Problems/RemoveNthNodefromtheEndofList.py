# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # take 2 pointers
        p1, p2 = head, head

        # phele n prr bhita diya
        for i in range(n):
            p2 = p2.next

        # corner case
        if p2 == None:
            head = head.next
            return head

        # dono koo sath mein shru kardiya
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next

        p1.next = p1.next.next

        # last mein head return kardiya
        return head




