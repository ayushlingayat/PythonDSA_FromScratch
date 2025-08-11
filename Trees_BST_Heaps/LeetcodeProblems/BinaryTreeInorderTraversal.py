# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorder(self, root):
        # Base Case
        if root is None:
            return
            # Recursive Case
        self.inorder(root.left)  # left subtree
        self.ans.append(root.val)
        self.inorder(root.right)  # right subtree

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.inorder(root)
        return self.ans


