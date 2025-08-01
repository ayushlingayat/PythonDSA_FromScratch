# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        hasCycle = False

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                hasCycle = True
                break

        if not hasCycle:
            return None

        len_ = 0
        while slow.next != fast:
            slow = slow.next
            len_ += 1

        len_ += 1
        slow = slow.next

        slow = head
        fast = head

        for i in range(len_):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow