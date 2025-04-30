# Last updated: 30/04/2025, 19:05:39
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        values = self.keyStore[key]
        i = bisect_right(values, (timestamp, chr(127)))
        if i == 0:
            return ""
        return values[i-1][1]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)