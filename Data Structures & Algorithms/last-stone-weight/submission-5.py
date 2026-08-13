class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        if len(max_heap) == 1:
            return -max_heap[0]
        while len(max_heap) > 1:
            y, x = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if y < x:
                heapq.heappush(max_heap, y - x)
        if not max_heap:
            return 0
        return -max_heap[0]

