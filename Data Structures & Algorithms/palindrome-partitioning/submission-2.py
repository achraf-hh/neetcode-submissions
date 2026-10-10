class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, cur = [], []

        def dfs(start):
            if start == len(s):
                res.append(cur.copy())
                return
            for cut in range(start+1, len(s)+1):
                sub = s[start:cut]
                if sub == sub[::-1]:
                    cur.append(sub)
                    dfs(cut)
                    cur.pop()
        dfs(0)
        return res
