class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return []
        exist = set(nums)
        for i in range(1, len(nums)+2):
            if i not in exist:
                return i
        