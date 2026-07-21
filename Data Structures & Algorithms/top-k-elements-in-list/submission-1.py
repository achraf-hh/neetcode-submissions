class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        freq = [[] for _ in range(len(nums) + 1)]
         
        for num in nums:
            occ[num] = 1 + occ.get(num, 0)
        for key in occ:
            freq[occ[key]].append(key)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        
        