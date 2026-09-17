class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        digits = set()
        for n in nums:
            if n in digits:
                return n
            else:
                digits.add(n)