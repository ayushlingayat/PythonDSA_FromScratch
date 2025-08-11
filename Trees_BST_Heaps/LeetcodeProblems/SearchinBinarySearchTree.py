# you can do it using recurssion or while loop did this using the while loop


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        curr = root
        while curr != None:
            if curr.val == target:
                return curr
            elif target < curr.val:
                # left subtree
                curr = curr.left
            else:
                # right subtree
                curr = curr.right

        return curr


