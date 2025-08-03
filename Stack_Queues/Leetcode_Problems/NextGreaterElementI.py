class Solution:
    def nextGreaterElement(self, nums1: List[int], arr: List[int]) -> List[int]:
        n = len(arr)
        ans = {}

        st = []

        for i in range(n - 1, -1, -1):
            while len(st) > 0 and st[-1] <= arr[i]:
                st.pop()
            if len(st) == 0:
                ans[arr[i]] = -1
            else:
                ans[arr[i]] = st[-1]

            st.append(arr[i])

        res = []
        for i in nums1:
            res.append(ans[i])

        return list(res)

