class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left+right)//2 
            ht = 0
            for i in range(len(piles)):
                hi = math.ceil(piles[i]/mid)
                ht += hi
            if ht <= h:
                right = mid 
            else: 
                left = mid + 1
        return right 