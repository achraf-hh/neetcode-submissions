class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longuest = 1
        elets = set(nums)
        for num in elets:
            if num - 1 not in elets:
                curr_num = num
                streak = 1
                while curr_num + 1 in elets:
                    streak += 1
                    curr_num = curr_num+1
                longuest = max(streak, longuest)
        return longuest