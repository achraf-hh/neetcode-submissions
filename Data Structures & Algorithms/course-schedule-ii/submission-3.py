class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)
        curr = set()
        vis = set()
        res = []

        def dfs(node):
            if node in curr: return -1
            if node in vis: return node
            curr.add(node)
            for p in preMap[node]:
                if dfs(p) == -1:
                    return -1
            curr.remove(node)
            vis.add(node)
            res.append(node)
            return node
        for crs in range(numCourses):
            if dfs(crs) == -1:
                return []
        return res