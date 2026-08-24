class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, columns = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(row, col):

            if row >= rows or row < 0 or col >= columns or col < 0 or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row+dr, col+dc)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and grid[r][c] != "0":
                    dfs(r,c)
                    islands += 1
        return islands
                    


                
