#power of 2 using while loop

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n%2 == 0:
            n//2
        return n ==1

#power of 2 using recurssion

