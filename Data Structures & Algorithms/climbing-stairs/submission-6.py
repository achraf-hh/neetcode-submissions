class Solution:
    def climbStairs(self, n: int) -> int:
        v1 = v2 = 1
        for i in range(2, n+1):
            tmp = v1 + v2
            v2, v1 = v1, tmp
        return v1