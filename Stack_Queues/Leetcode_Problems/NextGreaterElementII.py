class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        arr += arr
        n = len(arr)
        ans = [0] * n

        st = []

        for i in range(n - 1, -1, -1):
            while len(st) > 0 and st[-1] <= arr[i]:
                st.pop()
            if len(st) == 0:
                ans[i] = -1
            else:
                ans[i] = st[-1]

            st.append(arr[i])

        # res = []
        # for i in arr:
        #     res.append(ans[i])

        return list(ans[:n // 2])
