class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i, cur_target):
            if cur_target == 0: 
                res.append(cur.copy())
                return 
            elif cur_target < 0 or i == len(candidates):
                return
            cur.append(candidates[i])
            dfs(i+1, cur_target - candidates[i])
            cur.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, cur_target)
        candidates = sorted(candidates)
        dfs(0, target)
        return res
