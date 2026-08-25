class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea, tempArea = 0, 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            nonlocal tempArea
            if row < 0 or col < 0 or row >= rows or col >= columns or grid[row][col] == 0 or (row, col) in visited:
                return
            visited.add((row, col))

            for dr, dc in directions:
                dfs(row+dr, col+dc)
            tempArea += 1



        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
                    maxArea = max(maxArea, tempArea)
                    tempArea = 0


        return maxArea
