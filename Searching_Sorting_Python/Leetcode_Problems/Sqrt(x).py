class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0  # To store the result

        while l <= r:
            mid = (l + r) // 2
            midSquare = mid * mid

            if midSquare == x:
                return mid
            elif midSquare < x:
                ans = mid  # This could be the answer
                l = mid + 1
            else:
                r = mid - 1

        return ans
