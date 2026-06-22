class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        for row in matrix:
            n = len(row)
            left = 0
            right = n-1
            if row == []:
                return False
            while left <= right:
                mid = (left + right)//2
                if target < row[mid]:
                    right = mid - 1
                elif target > row[mid]:
                    left = mid + 1
                else:
                    return True
        return False