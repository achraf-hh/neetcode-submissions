class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r, maxLen = 0, 0, 0
        occ = {}
        while r < len(s):
            if s[r] in occ:
                occ[s[r]] += 1
            else:
                occ[s[r]] = 1
            maxi =  max(occ.values())
            mistake = r - l + 1 - maxi
            while mistake > k:
                occ[s[l]] -= 1
                l += 1
                maxi = max(occ.values())
                mistake = r - l + 1 - maxi
            maxLen = max(r - l + 1, maxLen)
            r += 1
        return maxLen

