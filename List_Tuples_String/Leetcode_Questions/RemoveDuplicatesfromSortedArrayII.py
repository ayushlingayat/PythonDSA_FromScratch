class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        # base case
        if n <= 2:
            return n

        start = 1
        for i in range(2, n):
            # unique element
            if nums[i] != nums[start - 1]:
                nums[start] += 1
                nums[start] = nums[i]

        return start + 1 
