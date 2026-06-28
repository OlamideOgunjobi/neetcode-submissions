class TimeMap:

    def __init__(self):
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = [(value, timestamp)]
        else:
            self.times[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""


        start = 0
        end = len(self.times[key]) - 1
        value = ""

        while start <= end:
            mid = (start + end) // 2

            if self.times[key][mid][1] <= timestamp:
                value = self.times[key][mid][0]
                start = mid + 1
            else: #self.times[key][mid][1] > timestamp
                end = mid - 1

        return value
            # if start == end:
            #     return self.times[key][start][0]
            # elif (self.times[key])[mid][1] == timestamp:
            #     return self.times[key][mid][0]
            # elif timestamp < (self.times[key])[mid][1]:
            #     end = mid - 1
            # elif timestamp > (self.times[key])[mid][1]:
            #     start = mid + 1

    

        