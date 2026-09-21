class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longuest = 1
        elets = set(nums)
        candidates = []
        for num in nums:
            if num - 1 not in elets : candidates.append(num)
            else: continue
        for c in candidates:
            ci = c
            temp = 1
            while ci + 1 in elets:
                temp += 1
                ci = ci+1
            longuest = max(longuest, temp)
        return longuest



