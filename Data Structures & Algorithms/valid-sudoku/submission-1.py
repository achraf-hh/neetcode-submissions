class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, sq = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sq[(r//3, c//3)]:
                        return False
                    else:
                        row[r].add(board[r][c])
                        col[c].add(board[r][c])
                        sq[(r//3, c//3)].add(board[r][c])
        return True
