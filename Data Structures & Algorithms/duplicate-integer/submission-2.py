class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        occ = defaultdict(int)
        for num in nums:
            occ[num] += 1
        for v in occ.values():
            if v > 1:
                return True
        return False