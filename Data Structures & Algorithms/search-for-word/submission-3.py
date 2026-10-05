class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (1,0), (0,1), (0, -1)]
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(row, col, i):
            if row >= rows or row < 0 or col >= cols or col < 0 or (row, col) in visit or board[row][col] != word[i]:
                return
            elif i == len(word) - 1:
                return True
            visit.add((row, col))
            for dr, dc in directions:
                new_r, new_c = row+dr, col+dc
                if  dfs(new_r, new_c, i+1):
                    return True
            visit.discard((row, col))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False