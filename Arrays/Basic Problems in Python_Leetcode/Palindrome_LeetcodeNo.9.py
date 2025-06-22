class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0

        while temp > 0:
            r = temp % 10
            temp = temp // 10
            rev = rev * 10 + r

        if rev == x:
            return True
        else:
            return False

        return rev == x