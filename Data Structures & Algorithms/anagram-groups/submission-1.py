class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        res = []
        hist = {}
        for i in range(len(strs)):
            occur = [0]*26
            for j in range(len(strs[i])):
                occur[ord(strs[i][j]) - 97] += 1
            occur_key = tuple(occur)
            if occur_key in hist:
                hist[occur_key].append(strs[i])
            else:
                hist[occur_key] = [strs[i]]
        for v in hist.values():
            res.append(v)
        return res
