class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visit = set()
        res, cur = [], []

        def dfs():
            for i in range(len(nums)):
                if nums[i] not in visit:
                    visit.add(nums[i])
                    cur.append(nums[i])
                    dfs()
                else:
                    continue
                if len(cur) == len(nums):
                    res.append(cur.copy())
                visit.remove(nums[i])
                cur.pop()

        dfs()
        return res