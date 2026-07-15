class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        for letter in t:
            if s and s[0] == letter:
                s= s[1:]
        if s:
            return False
        else:
            return True