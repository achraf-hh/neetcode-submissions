class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(row, col):
            if row >=rows or row < 0 or col >=cols or col < 0 or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            tempArea = 0
            for dr, dc in directions:
                tempArea += dfs(row+dr, col+dc)
            return 1 + tempArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r,c), maxArea)
        return maxArea