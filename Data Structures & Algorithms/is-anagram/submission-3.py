class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        Smap = {}
        Tmap = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            Smap[s[i]] = 1 + Smap.get(s[i],0)
            Tmap[t[i]] = 1 + Tmap.get(t[i],0)

        if Smap == Tmap:
            return True

        return False

        