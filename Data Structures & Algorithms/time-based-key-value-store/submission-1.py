class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        res = ""
        lo, hi = 0, len(self.timeMap[key])-1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.timeMap[key][mid][1] < timestamp:
                res = self.timeMap[key][mid][0]
                lo = mid + 1 
            elif self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]
            else:
                hi = mid - 1

        return res

