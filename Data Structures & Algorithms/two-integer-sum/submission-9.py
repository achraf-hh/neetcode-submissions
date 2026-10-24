class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elets_map = defaultdict(int)
        res = []
        for i in range(len(nums)):
            elets_map[nums[i]] = i
        for i in range(len(nums)):
            can = target - nums[i]
            if can in elets_map and elets_map[can] != i:
                res.append(min(i, elets_map[can]))
                res.append(max(i, elets_map[can]))
                break
        return res



        