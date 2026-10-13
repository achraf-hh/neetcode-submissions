class Solution:
    def climbStairs(self, n: int) -> int:
        m1 = m2 = 1
        for _ in range(2, n+1):
            ways = m1+m2
            m1, m2 = ways, m1
        return m1