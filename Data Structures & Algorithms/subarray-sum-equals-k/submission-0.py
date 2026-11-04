class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = 0
        track = {0:1}
        for n in nums:
            prefix+=n
            ans += track.get(prefix-k, 0)
            track[prefix] = track.get(prefix, 0) + 1
        return ans