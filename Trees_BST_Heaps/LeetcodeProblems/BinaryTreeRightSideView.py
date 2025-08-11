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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
                level.append(front.val)  #only append current node's value
                if front.left is not None:
                    queue.push(front.left)
                if front.right is not None:
                    queue.push(front.right)

            ans.append(level[-1])  #rightmost node at this level

        return ans
