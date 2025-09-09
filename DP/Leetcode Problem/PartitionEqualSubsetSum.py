from typing import List

class Solution:
    def rec(self, i, target, nums, dp):
        # base cases
        if target == 0:
            return True
        if i == 0:
            return nums[0] == target

        if dp[i][target] != -1:
            return dp[i][target]

        not_take = self.rec(i-1, target, nums, dp)
        take = False
        if nums[i] <= target:
            take = self.rec(i-1, target - nums[i], nums, dp)

        dp[i][target] = take or not_take
        return dp[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return False

        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = [[-1] * (target + 1) for _ in range(n)]

        return self.rec(n-1, target, nums, dp)
