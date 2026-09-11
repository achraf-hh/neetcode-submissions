class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()
        neiMap = defaultdict(list)
        for e, d in edges:
            neiMap[e].append(d)
            neiMap[d].append(e)
        currPath = []

        def dfs(node, prev):
            if node in visit:
                idx = currPath.index(node)
                cycleNodes = currPath[idx:]
                cycleEdges = set()
                for i in range(len(cycleNodes)-1):
                    cycleEdges.add((min(cycleNodes[i], cycleNodes[i+1]), max(cycleNodes[i], cycleNodes[i+1])))
                cycleEdges.add((min(cycleNodes[0], cycleNodes[-1]), max(cycleNodes[0], cycleNodes[-1])))
                for i in range(len(edges)-1, 0, -1):
                    if tuple(edges[i]) in cycleEdges:
                        return edges[i]
            else:
                visit.add(node)
                currPath.append(node)
                for nei in neiMap[node]:
                    if nei == prev: continue
                    else:
                        ans = dfs(nei, node)
                        if ans:
                            return ans
                currPath.pop()


        return dfs(1, -1)

                
