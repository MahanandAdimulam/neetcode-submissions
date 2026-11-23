class TimeMap:

    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        start, end = 0, len(arr) - 1
        result = ""

        while start <= end:
            mid = (start + end) // 2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]   # valid candidate, but look for a later one
                start = mid + 1
            else:
                end = mid - 1

        return result