class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        borders = []
        for r in range(rows):
            borders.append((r,0))
            borders.append((r, cols-1))
        for c in range(cols):
            borders.append((0,c))
            borders.append((rows-1,c))
        
        def dfs(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0 or   board[row][col] == 'X':
                return
            if board[row][col] == 'O':
                board[row][col] = 'M'
                for dr, dc in directions:
                    new_r, new_c = row+dr, col+dc
                    dfs(new_r, new_c)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in borders and board[r][c] == 'O':
                    dfs(r,c)
        for r in range(rows):
            for c in range(cols):
                    if board[r][c] == 'O':
                        board[r][c] = 'X'
                    elif board[r][c] == 'M':
                        board[r][c] = 'O'
