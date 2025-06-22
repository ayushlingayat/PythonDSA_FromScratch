from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = []

        for i in candies:
            if (i + extraCandies) >= maxCandies:
                ans.append(True)
            else:
                ans.append(False)

        return ans
