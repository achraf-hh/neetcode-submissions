class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left = 0
        right = m*n - 1
        
        while left <= right:
            mid = (right+left)//2
            if target == matrix[mid//n][mid%n]:
                return True
            elif target < matrix[mid//n][mid%n]:
                right = mid - 1
            else:
                left = mid + 1
        return False

        