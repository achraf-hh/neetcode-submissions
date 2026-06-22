class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        n = len(nums)
        mid = n//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            result = self.search(nums[mid+1:], target)
            if result == -1:
                return result
            return result + mid + 1
            
        else:
            result = self.search(nums[:mid], target)
            return result
        return -1