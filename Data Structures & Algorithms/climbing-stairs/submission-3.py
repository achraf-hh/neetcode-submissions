class Solution:
    def climbStairs(self, n: int) -> int:
        f_minus1 = f_minus2 = 1
        for i in range(2, n+1):
            ways = f_minus1 + f_minus2
            f_minus1, f_minus2 = ways, f_minus1
        return f_minus1
            