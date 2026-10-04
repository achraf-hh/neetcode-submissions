class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols = len(board), len(board[0])
        visit = set()
        letters = set(word)


        def dfs(r, c, i):
            if r >= rows or r < 0 or c < 0 or c >= cols or (r,c) in visit or board[r][c] != word[i]:
                return 
            elif i == len(word) - 1:
                return True

            visit.add((r,c))
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if dfs(new_r, new_c, i+1):
                   return True 

            visit.discard((r,c))
            return False
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
                