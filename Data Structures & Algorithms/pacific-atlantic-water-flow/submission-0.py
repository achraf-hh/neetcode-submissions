class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pac, atl = [], []
        for c in range(cols):
            pac.append((0, c))
            atl.append((rows-1, c))
        for r in range(rows):
            pac.append((r, 0))
            atl.append((r, cols-1))
        pac_vis, atl_vis = set(), set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        

        def dfs(row, col, visited, prev_height):
            if row >= rows or row < 0 or col >= cols or col < 0 or (row, col) in visited or heights[row][col] < prev_height:
                return
            visited.add((row, col))
            for dr, dc in directions:
                new_r, new_c = row+dr, col+dc
                dfs(new_r, new_c, visited, heights[row][col])
            
        for r, c in pac:
            dfs(r,c, pac_vis, 0)
        for r,c in atl:
            dfs(r,c, atl_vis, 0)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac_vis and (r,c) in atl_vis:
                    res.append([r,c])
        return res


        