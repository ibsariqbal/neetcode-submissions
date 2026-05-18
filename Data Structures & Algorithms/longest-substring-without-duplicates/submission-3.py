class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            #mp[s[r]] = mp.get(s[r], 0) + 1
            if s[r] in mp:
                mp[s[r]]+=1
            else:
                mp[s[r]] = 1

            while mp[s[r]] > 1:
                mp[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
            


                