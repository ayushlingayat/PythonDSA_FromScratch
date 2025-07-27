#Insertion Sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(1, n):
            key = nums[i]        # Store the current element
            j = i - 1

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]  # Shift larger elements to the right
                j -= 1

            nums[j + 1] = key  # Insert the key in the correct position

        return nums

"""
🧠 Dry Run of Insertion Sort:

Given: nums = [5, 2, 4, 6, 1]
n = 5

Initial: [5, 2, 4, 6, 1]

Pass 1 (i = 1, key = 2):
    j = 0 → 5 > 2 → shift → [5, 5, 4, 6, 1]
    j = -1 → stop
    Insert key → [2, 5, 4, 6, 1]

Pass 2 (i = 2, key = 4):
    j = 1 → 5 > 4 → shift → [2, 5, 5, 6, 1]
    j = 0 → 2 < 4 → stop
    Insert key → [2, 4, 5, 6, 1]

Pass 3 (i = 3, key = 6):
    j = 2 → 5 < 6 → stop
    Insert key → [2, 4, 5, 6, 1] (no change)

Pass 4 (i = 4, key = 1):
    j = 3 → 6 > 1 → shift → [2, 4, 5, 6, 6]
    j = 2 → 5 > 1 → shift → [2, 4, 5, 5, 6]
    j = 1 → 4 > 1 → shift → [2, 4, 4, 5, 6]
    j = 0 → 2 > 1 → shift → [2, 2, 4, 5, 6]
    j = -1 → stop
    Insert key → [1, 2, 4, 5, 6]

✅ Final Sorted Array: [1, 2, 4, 5, 6]
Time Complexity: 
    Best case: O(n) when already sorted
    Average/Worst: O(n^2)
Space Complexity: O(1)
Stable: Yes ✅
In-place: Yes ✅
"""


# ❓ Q1: What is the time complexity of Insertion Sort?
# Answer:
#
# Best case: O(n) → when the array is already sorted
#
# Average case: O(n²)
#
# Worst case: O(n²) → when the array is sorted in reverse
#
# ❓ Q2: Why is Insertion Sort useful?
# Answer:
#
# It's good for small datasets
#
# Works well when data is nearly sorted
#
# It is stable and in-place
#
# Useful in hybrid sorting algorithms (like Python’s Timsort)
#
# ❓ Q3: Can Insertion Sort be used in real-time streaming?
# Answer:
#
# Yes — for small windows of streaming data, Insertion Sort is simple and efficient because:
#
# New elements can be inserted in O(n) time
#
# It avoids expensive overhead of more complex algorithms
#
# ❓ Q4: Is Insertion Sort stable and in-place?
# Answer:
#
# Stable: Yes — equal elements retain their relative order
#
# In-place: Yes — it doesn’t use extra space
