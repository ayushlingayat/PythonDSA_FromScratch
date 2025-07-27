from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            isSwap = False
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    # swap
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                    isSwap = True

            if not isSwap:
                break

        return nums

"""
Dry Run of Bubble Sort:

Given: nums = [5, 1, 4, 2, 8]
n = 5

Initial: [5, 1, 4, 2, 8]

Pass 1 (i = 0):
    j = 0: 5 > 1 → swap → [1, 5, 4, 2, 8]
    j = 1: 5 > 4 → swap → [1, 4, 5, 2, 8]
    j = 2: 5 > 2 → swap → [1, 4, 2, 5, 8]
    j = 3: 5 < 8 → no swap
Result after pass 1: [1, 4, 2, 5, 8]

Pass 2 (i = 1):
    j = 0: 1 < 4 → no swap
    j = 1: 4 > 2 → swap → [1, 2, 4, 5, 8]
    j = 2: 4 < 5 → no swap
Result after pass 2: [1, 2, 4, 5, 8]

Pass 3 (i = 2):
    j = 0: 1 < 2 → no swap
    j = 1: 2 < 4 → no swap
Result after pass 3: [1, 2, 4, 5, 8]

Pass 4 (i = 3):
    j = 0: 1 < 2 → no swap
Result after pass 4: [1, 2, 4, 5, 8]

✅ Final Sorted Array: [1, 2, 4, 5, 8]
Time Complexity: O(n^2) worst case
Stable Sort: Yes
In-place Sort: Yes
"""


# Bubble Sort Time Complexity:
# Case	Comparisons
# Best Case	O(n) → when array is already sorted (with optimization)
# Average	O(n²)
# Worst Case	O(n²)
