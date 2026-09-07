class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        vis = set()
        neiMap = defaultdict(list)
        for e, d in edges:
            neiMap[e].append(d)
            neiMap[d].append(e)
        def dfs(curr, prev):
            if curr in vis:
                return False
            vis.add(curr)
            for i in neiMap[curr]:
                if i in vis:
                    if i != prev:
                        return False
                    else: continue
                if not dfs(i, curr):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(vis) == n