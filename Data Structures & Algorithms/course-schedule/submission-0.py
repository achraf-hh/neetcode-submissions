class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for c, p in prerequisites:
            prereq[c].append(p)
        explored, still = set(), set()

        def dfs(curr):
            if curr in explored:
                return True
            if curr in still: 
                return False
            still.add(curr)
            for p in prereq[curr]:
                if not dfs(p):
                    return False
            still.remove(curr)
            explored.add(curr)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True





        