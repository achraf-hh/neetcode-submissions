class TimeMap:

    def __init__(self):
        self.timeMap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timeMap:
            self.timeMap[key] = [[value, timestamp]]
        else: 
            self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timeMap:
            return ""
        left = 0
        right = len(self.timeMap[key]) - 1
        result = ""
        while left <= right:
            mid = (left+right)//2
            if self.timeMap[key][mid][1] < timestamp:
                result = self.timeMap[key][mid][0]
                left = mid + 1
            elif self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]
            else:
                right = mid - 1

        return result
        
