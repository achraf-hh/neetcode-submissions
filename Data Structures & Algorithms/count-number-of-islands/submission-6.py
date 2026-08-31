class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]

        def dfs(row, col):
            if row >= rows or row <0 or col >= cols or col <0 or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row+dr, col+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands