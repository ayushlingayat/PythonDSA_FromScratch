#Selection Sort
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            min_val = nums[i]  # Assume the current index has the min
            ind = i
            for j in range(i + 1, n):
                if nums[j] < min_val:
                    min_val = nums[j]
                    ind = j  # Update index of the smallest value

            # Swap the current element with the found minimum
            nums[i], nums[ind] = nums[ind], nums[i]

        return nums

"""
🧠 Dry Run of Selection Sort:

Given: nums = [64, 25, 12, 22, 11]
n = 5

Initial: [64, 25, 12, 22, 11]

Pass 1 (i = 0):
    min_val = 64
    Loop j = 1 to 4 → new min = 11 at index 4
    Swap 64 and 11 → [11, 25, 12, 22, 64]

Pass 2 (i = 1):
    min_val = 25
    Loop j = 2 to 4 → new min = 12 at index 2
    Swap 25 and 12 → [11, 12, 25, 22, 64]

Pass 3 (i = 2):
    min_val = 25
    Loop j = 3 to 4 → new min = 22 at index 3
    Swap 25 and 22 → [11, 12, 22, 25, 64]

Pass 4 (i = 3):
    min_val = 25
    Loop j = 4 → 25 < 64 → no change
    [11, 12, 22, 25, 64]

Pass 5 (i = 4): Last element → no need to sort

✅ Final Sorted Array: [11, 12, 22, 25, 64]
Time Complexity: O(n²)
Space Complexity: O(1)
Stable: ❌ No (can break the order of equal elements)
In-place: ✅ Yes
"""

# ❓ Q1: What's the time and space complexity?
# Answer:
#
# Time: O(n²) in all cases (best, worst, average)
#
# Space: O(1) (in-place)
#
# Not stable by default
