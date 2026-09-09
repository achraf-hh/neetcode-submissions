class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        neiMap = defaultdict(list)
        for e, d in edges:
            neiMap[e].append(d)
            neiMap[d].append(e)
        res = 0
        def dfs(curr):
            if curr in visited:
                return 
            visited.add(curr)
            for nei in neiMap[curr]:
                if nei in visited:
                    continue
                else: dfs(nei)
        for i in range(n):
            if i in visited:
                continue
            else:
                dfs(i)
                res += 1
        return res