class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            #nonlocal tempArea
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row, col) in visited:
                return 0
            visited.add((row, col))
            tempArea = 0
            for dr, dc in directions:
                tempArea += dfs(row+dr, col+dc)
            return 1 + tempArea

            #tempArea += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    #dfs(r,c)
                    maxArea = max(dfs(r,c), maxArea)
                    #tempArea = 0
        return maxArea