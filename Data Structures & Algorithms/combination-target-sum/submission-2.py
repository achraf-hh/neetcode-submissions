class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i, cur_target):
            if cur_target == 0:
                res.append(cur.copy())
                return
            elif cur_target < 0 or i == len(nums):
                return
            cur.append(nums[i])
            dfs(i, cur_target-nums[i])
            cur.pop()
            dfs(i+1, cur_target)
        
        dfs(0, target)
        return res

