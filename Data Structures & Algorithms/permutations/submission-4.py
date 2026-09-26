class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        visit = set()
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in visit:
                    visit.add(nums[i])
                    cur.append(nums[i])
                    dfs()
                    cur.pop()
                    visit.remove(nums[i])
        dfs()
        return res