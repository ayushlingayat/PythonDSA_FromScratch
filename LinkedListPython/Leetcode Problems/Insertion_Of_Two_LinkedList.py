# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        c = 0

        while p1 != p2:
            if p1 is None:
                p1 = headB
                c += 1
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

            if c > 1:
                return None

        return p1

