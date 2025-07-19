class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s.reverse()
        return " ".join(s)

        return " ".join(s)

# Do this without Inbuild method

class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        word = ''
        for i in s:
            if i != ' ':
                word += i
            elif word:
                l.append(word)
                word = ''
        if word:
            l.append(word)

        i = 0
        j = len(l) - 1

        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

        s = ''
        for i in range(len(l)):
            if i < len(l) - 1:
                s += l[i] + ' '
            else:
                s += l[i]

        return s