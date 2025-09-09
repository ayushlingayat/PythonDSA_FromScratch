from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()       # backtrack
                    used[i] = False  # reset choice

        backtrack([], [False]*len(nums))
        return res

print(Solution().permute([1,2,3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
