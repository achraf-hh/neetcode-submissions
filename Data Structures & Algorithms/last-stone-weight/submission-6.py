class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y, x = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if y < x:
                heapq.heappush(max_heap, y - x)
        heapq.heappush(max_heap, 0)
        return -max_heap[0]
