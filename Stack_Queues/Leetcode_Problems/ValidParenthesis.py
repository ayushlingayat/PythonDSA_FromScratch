class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "{":"}", "[":"]"}  # mapping of opening → closing
        stack = []

        for char in s:
            if char in d:  # it's an opening bracket
                stack.append(char)  # push to stack
            else:  # it's a closing bracket
                if not stack or d[stack.pop()] != char:
                    return False  # mismatch or empty stack
        return not stack


