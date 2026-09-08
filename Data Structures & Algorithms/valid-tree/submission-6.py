class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        visit  = set()
        neiMap = defaultdict(list)
        for e, d in edges:
            neiMap[e].append(d)
            neiMap[d].append(e)
        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for nei in neiMap[curr]:
                if nei in visit:
                    if nei != prev:
                        return False
                    else: continue
                if not dfs(nei, curr):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visit) == n 