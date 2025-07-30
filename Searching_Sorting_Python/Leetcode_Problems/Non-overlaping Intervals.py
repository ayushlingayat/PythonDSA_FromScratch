class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals koo first sort karna hee hume on the basis of 1 element
        # yeeh list of list hee so directly sort toh nhi hogi okk
        # so hume naa lamda function use karna hoga

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)  # total no of elements in the interval yeeh nikal liya

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                count += 1
                prev = i

        return n - count  # vooh elements mil jayenge joo consider nhi karne the

    