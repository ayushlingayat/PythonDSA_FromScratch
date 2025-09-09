from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()  # backtrack

        backtrack(1, [])
        return res

print(Solution().combine(4, 2))
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
