class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[0]
        
        while left < right:
            mid = (right+left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 

        return nums[right]

            

