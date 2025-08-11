# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True

    def height(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        # left subtree height
        leftHeight = self.height(root.left)
        # right subtree height
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.ans = False
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
