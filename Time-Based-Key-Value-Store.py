class TimeMap:

    def __init__(self):
        self.timestamps = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        keyArr = self.timestamps[key]

        l = 0
        r = len(keyArr) - 1

        while l <= r:
            mid = (l + r) // 2
            if keyArr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if r < 0:
            return ""
        return keyArr[r][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)