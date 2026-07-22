class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            tot_h = 0
            for i in range(len(piles)):
                hi = math.ceil(piles[i]/mid)
                tot_h += hi
            if tot_h <= h:
                r = mid
            else:
                l = mid + 1
        return r