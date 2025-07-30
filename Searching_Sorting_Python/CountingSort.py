#use for defining limits and count
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mx = max(nums)

        freq = [0] * (mx + 1)

        for i in nums:
            freq[i] += 1

        nums = []

        for i in range(0, mx + 1):
            while freq[i] > 0:
                nums.append(i)
                freq[i] -= 1

        return nums

# TC - O(n) /O(mx)
# SC - O(mx)
