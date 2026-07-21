class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hist = defaultdict(list)

        for s in strs:
            occur = [0]*26
            for char in s:
                occur[ord(char) - 97] +=1
            hist[tuple(occur)].append(s)
        return list(hist.values())
