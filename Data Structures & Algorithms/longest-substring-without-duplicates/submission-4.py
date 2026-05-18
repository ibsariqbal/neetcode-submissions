class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            #mp[s[r]] = mp.get(s[r], 0) + 1
            if s[r] in mp:
                l = max(mp[s[r]]+1,l)

            mp[s[r]] = r

            longest = max(longest, r - l + 1)

        return longest
            


                