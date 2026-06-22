class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        exists = False
        for row in matrix:
            n = len(row)
            left = 0
            right = n-1
            
            if row == []:
                return False
            if len(row) == 1 and row[0] == target:
                exists = True
                break
            
            while left <= right:
                mid = (left + right)//2
                if target < row[mid]:
                    right = mid - 1
                elif target > row[mid]:
                    left = mid + 1
                else:
                    exists = True
                    break

        
        
        return exists