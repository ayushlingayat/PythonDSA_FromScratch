# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q = []
        self.front = 0

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if self.front >= len(self.q):
            return -1
        x = self.q[self.front]
        self.front += 1
        return x

    def getFront(self):
        if self.front >= len(self.q):
            return -1
        return self.q[self.front]

    def size(self):
        return len(self.q) - self.front


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = Queue()
        ans = []

        queue.push(root)
        ans.append([root.val])

        while queue.size() > 0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)

            if len(level) > 0:
                ans.append(level)

        ans.reverse()
        return ans




