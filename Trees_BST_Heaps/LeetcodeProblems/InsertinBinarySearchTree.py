# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        newNode = TreeNode(target)

        if root is None:
            return newNode

        curr = root
        while curr != None:
            if target < curr.val:
                # left subtree
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            else:
                # right subtree
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break

        return root


