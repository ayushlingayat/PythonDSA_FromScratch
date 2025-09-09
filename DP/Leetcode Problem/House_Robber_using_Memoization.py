class Solution:

    def rec(self, i, nums):
        # base case
        if i >= len(nums):
            return 0

        if dp[i] != -1:
            return dp[i]

        # take case
        take = nums[i] + self.rec(i + 2, nums, dp)

        # not take case
        not_take = self.rec(i + 1, nums, dp)

        dp[i] = max(take, not_take)

        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.rec(0, nums, dp)

