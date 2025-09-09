class Solution:

    def rec(self, i, nums):
        # base case
        if i >= len(nums):
            return 0
        # take case
        take = nums[i] + self.rec(i + 2, nums)
        # not take case
        not_take = self.rec(i + 1, nums)

        return max(take, not_take)

    def rob(self, nums: List[int]) -> int:
        return self.rec(0, nums)

