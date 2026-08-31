class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, minutes = 0, 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q :
            for _ in range(len(q)):
                ro, co = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = ro+dr, co+dc
                    if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        fresh -= 1
            minutes += 1   
            
        return -1 if fresh > 0   else max(0, minutes-1)




                                