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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = Queue()
        ans = []

        queue.push(root)

        while queue.size() > 0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                level.append(front.val)  # store current node's value here
                if front.left is not None:
                    queue.push(front.left)
                if front.right is not None:
                    queue.push(front.right)

            if len(ans) % 2 == 1:  # reverse on odd levels
                level.reverse()

            ans.append(level)

        return ans

