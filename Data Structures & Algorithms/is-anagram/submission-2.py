class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ_s = {}
        occ_t = {}
        for si in s:
            if si in occ_s:
                occ_s[si] += 1
            else:
                occ_s[si] = 1
        for ti in t:
            if ti in occ_t:
                occ_t[ti] += 1
            else:
                occ_t[ti] = 1
        return occ_s == occ_t