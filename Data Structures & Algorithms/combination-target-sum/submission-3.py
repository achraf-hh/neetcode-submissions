class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur, res = [], []

        def dfs(i, cur_target):
            if cur_target == 0:
                res.append(cur.copy())
                return
            elif i == len(nums) or cur_target < 0:
                return 
            cur.append(nums[i])
            dfs(i, cur_target-nums[i])
            cur.pop()
            dfs(i+1, cur_target)
        dfs(0, target)
        return res