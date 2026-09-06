class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for c, p in prerequisites :
            preMap[c].append(p)
        curr = set()

        def dfs(node):
            if node in curr: return False
            if preMap[node] == []: return True
            curr.add(node)
            for p in preMap[node]:
                if not dfs(p):
                    return False
            curr.remove(node)
            preMap[node] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True