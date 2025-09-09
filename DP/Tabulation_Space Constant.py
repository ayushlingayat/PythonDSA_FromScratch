class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 0 or n == 1:
            return n

        a = 0
        b = 1

        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return b

