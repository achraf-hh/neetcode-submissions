class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        elif len(nums) == 1 and target == nums[0]:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right+left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                        
        return -1    