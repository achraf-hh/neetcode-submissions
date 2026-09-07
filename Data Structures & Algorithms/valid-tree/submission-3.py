class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        neiMap = defaultdict(list)
        for e , d in edges:
            neiMap[e].append(d)
            neiMap[d].append(e)
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for i in neiMap[node]:
                if i in visit:
                    if i != parent:
                        return False
                    else : continue
                if not dfs(i, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visit) == n