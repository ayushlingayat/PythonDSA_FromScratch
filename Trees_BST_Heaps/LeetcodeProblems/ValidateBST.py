# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, mn, mx):
        if root is None:
            return True
        if root.val < mn or root.val > mx:
            return False

        checkLeft = self.check(root.left, mn, root.val - 1)
        checkRight = self.check(root.right, root.val + 1, mx)

        return checkLeft and checkRight

    # mn - means min
    # mx - means max
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -100000000000000, 100000000000000)
