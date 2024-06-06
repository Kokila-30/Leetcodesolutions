class Solution:
    def isPalindrome(self, x: int) -> bool:
        t:bool = True
        s = str(x)
        last = len(s)-1
        for i in range(len(s)):
            if s[i] != s[last]:
                t = False
                break
            last -= 1
        return t
