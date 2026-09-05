class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, curr = set(), set()
        preMap = defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)

        def dfs(node):
            nonlocal res
            if node in visited:
                return node
            if node in curr:
                return -1
            curr.add(node)
            for p in preMap[node]:
                if dfs(p) == -1:
                    return -1
            curr.remove(node)
            visited.add(node)
            res.append(node)
            return node
        for crs in range(numCourses):
            if dfs(crs) == -1:
                return []
        return res
        