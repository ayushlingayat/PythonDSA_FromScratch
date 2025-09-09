class Solution:
    def rec(self, n, dp):
        # Step 2 : Passing it everywhere
        # base case
        if n == 0 or n == 1:
            return n
        #Step 4 : check the dp array if not -1
        if dp[n]!= -1:
            return dp[n]


        # recursive case
        #Step 3 :assign to dp array
        dp[n] = self.rec(n - 1, dp) + self.rec(n - 2, dp)
        return dp[n]

    def fib(self, n: int) -> int:
        # Step 1 : Create a dp array
        dp = [-1] * (n + 1)
        return self.rec(n, dp)