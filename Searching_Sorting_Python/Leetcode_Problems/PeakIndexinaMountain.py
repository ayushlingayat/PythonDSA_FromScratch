class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                # You are in the increasing part of the mountain, so move right
                l = mid + 1
            else:
                # You are in the decreasing part of the mountain, or at the peak
                r = mid

        # At the end of the loop, l == r and pointing to the peak index
        return l

