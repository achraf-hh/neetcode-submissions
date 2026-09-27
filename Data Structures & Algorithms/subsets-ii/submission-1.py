class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr, res = [], []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j+=1 
            dfs(j)
        nums = sorted(nums)
        dfs(0)
        return res