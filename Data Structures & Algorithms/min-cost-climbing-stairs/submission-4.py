class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        v2, v1 = cost[1], cost[0]
        for i in range(2, n):
            tmp = cost[i] + min(v1, v2)
            v1, v2 = v2, tmp
        return min(v1, v2)


            
