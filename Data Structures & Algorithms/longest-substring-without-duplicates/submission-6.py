class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        hist = set(s[0])
        l = maxLen = 0
        r = 1
        while r < len(s):
            if s[r] in hist:
                maxLen = max(r - l, maxLen)
                while s[r] in hist:
                    hist.remove(s[l])
                    l += 1
            maxLen = max(r -l + 1, maxLen)
            hist.add(s[r])
            r += 1
        return maxLen
                


        