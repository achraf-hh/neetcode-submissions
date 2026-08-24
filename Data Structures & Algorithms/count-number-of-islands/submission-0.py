class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        q = deque()
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(grid)
        columns = len(grid[0])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
                    while q:
                        ro, col = q.popleft()
                        for dr, dc in directions:
                            new_r = ro + dr
                            new_c = col + dc
                            if (new_r >= 0 and new_r < rows) and (new_c >= 0 and new_c < columns):
                                if grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                                    q.append((new_r, new_c))
                                    visited.add((new_r, new_c))
                    islands += 1
        return islands

