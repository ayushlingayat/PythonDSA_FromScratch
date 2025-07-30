class Solution:
    # yeeh function array ko do part mein partition karta hee
    def partition(self, nums, l, r):
        key = nums[r]
        start = l

        for i in range(l, r + 1):
            if nums[i] <= key:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
        # yaha key seeh bade elem right mein aa jayenge and key seeh chote elem aajayenge in the left thik
        return start - 1  # yeeh start point return karega jisko hum bolte point p okk

    def quickSort(self, nums, l, r):
        # base case
        if l >= r:
            return

        # recursive case
        p = self.partition(nums, l, r)  # 🔧 Fixed typo here: 'partiton' ➝ 'partition'

        self.quickSort(nums, l, p - 1)
        self.quickSort(nums, p + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quickSort(nums, 0, n - 1)

        return nums

#  2. Time & Space Complexity Questions
# You’ll often be asked:
#
# What is the time complexity of Quicksort?
#
# Scenario	Time Complexity
# Best Case (balanced partitions)	O(n log n)
# Average Case	O(n log n)
# Worst Case (already sorted or all same elements)	O(n²)

# What is the space complexity?
#
# O(log n) (for recursive call stack in average case)
#
# O(n) worst-case if using additional arrays (not in your code — you did it in-place ✅)