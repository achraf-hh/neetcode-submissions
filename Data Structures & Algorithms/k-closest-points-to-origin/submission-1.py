class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        min_heap = [(p[0]**2+p[1]**2,p) for p in points]
        heapq.heapify(min_heap)
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res