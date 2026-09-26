class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []

        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return 
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j+=1
            dfs(j)
        nums = sorted(nums)
        dfs(0)
        return res