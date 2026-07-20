class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        hist = set(s[0])
        maxLen = 0
        l, r = 0, 1
        while r < len(s):
            while s[r] in hist:
                hist.remove(s[l])
                maxLen = max(r - l  , maxLen)
                l += 1
            if s[r] not in hist:
                hist.add(s[r])
                maxLen = max(r - l + 1, maxLen)
            r +=1
        return maxLen

                


        