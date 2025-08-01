# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head1
        curr2 = head2

        ans = ListNode(-1)
        carry = 0
        curr3 = ans

        while curr1 != None or curr2 != None:
            total = carry
            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next
            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next

            # carrying karne kee liye likha yeeh thik hee
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0

            # abb ans vale node mein dalne kee liye yeeh process
            newNode = ListNode(total)
            curr3.next = newNode  # curr3 kee next mein new node daldo
            curr3 = curr3.next  # moving curr3 forward

        # if carry is left after both lists are exhausted
        if carry > 0:
            newNode = ListNode(carry)
            curr3.next = newNode

        return ans.next
