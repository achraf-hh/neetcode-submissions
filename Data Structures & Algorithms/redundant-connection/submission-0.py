class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = set()
        currPath = []
        neiMap = defaultdict(list)
        for e, d in edges:
            neiMap[e].append(d)
            neiMap[d].append(e)
        def dfs(node, prev):
            if node in visit:
                idx = currPath.index(node)
                cycle = currPath[idx:]
                cycle_edges = set()
                for i in range(1,len(cycle)):
                    cycle_edges.add((min(cycle[i - 1], cycle[i]), max(cycle[i - 1], cycle[i])))
                cycle_edges.add((min(cycle[0], cycle[-1]), max(cycle[0], cycle[-1])))
                for i in range(len(edges) - 1, 0, -1):
                    if tuple(edges[i]) in cycle_edges:
                        return edges[i]
            else:
                visit.add(node)
                currPath.append(node)
                for nei in neiMap[node]:
                    if nei == prev: continue
                    else:
                        ans =  dfs(nei, node)
                        if ans:
                            return ans
                            

                currPath.pop(currPath.index(node))
        return dfs(1, -1)


