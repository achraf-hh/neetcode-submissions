class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        nodeMap = defaultdict(list)
        for e, d in edges:
            nodeMap[e].append(d)
            nodeMap[d].append(e)

        
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for i in nodeMap[node]:
                if i in visit and parent != i:
                    return False
                else:
                    dfs(i, node)
            return True

        if not dfs(0, -1):
            return False

        return len(visit) == n

        