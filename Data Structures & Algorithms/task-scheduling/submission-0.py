class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        occ_map = defaultdict(int)
        for t in tasks:
            occ_map[t] += 1
        max_heap = [-v for v in occ_map.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            if max_heap:
                val = heapq.heappop(max_heap)
                if val != -1:
                    q.append((val+1, time+n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q[0][0])
                q.popleft()
            time += 1
        return time


