class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+2)
        dp[2] = nums[0]
        for i in range(3, n+2):
            dp[i] = max(dp[i-2]+nums[i-2], dp[i-3]+nums[i-3])

        return dp[-1]
        