from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr):
            a, b = 0, 0  # a = dp[i-2], b = dp[i-1]
            for num in arr:
                new_b = max(b, a + num)
                a, b = b, new_b
            return b

        # Case 1: Exclude last house
        case1 = rob_linear(nums[:-1])
        # Case 2: Exclude first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)


