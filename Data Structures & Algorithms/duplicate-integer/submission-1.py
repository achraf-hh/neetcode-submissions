class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        occ = {}
        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        for v in occ.values():
            if v > 1:
                return True
        return False