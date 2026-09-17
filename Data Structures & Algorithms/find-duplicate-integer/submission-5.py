class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]

        slow, fast = nums[0], nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

        