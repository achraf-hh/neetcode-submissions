class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        res = []
        for i in range(len(nums)):
            vals[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in vals and vals[val] != i:
                res.append(min(i, vals[val]))
                res.append(max(i, vals[val]))
                break
        return res