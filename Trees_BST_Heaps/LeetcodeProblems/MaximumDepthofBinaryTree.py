# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        # left subtree height
        leftHeight = self.maxDepth(root.left)
        # right subtree height
        rightHeight = self.maxDepth(root.right)

        return max(leftHeight, rightHeight) + 1

