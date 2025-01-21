class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x:x[0])
        result.append(intervals[0])
        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1] = [result[-1][0], max(interval[1], result[-1][1])]
            else:
                result.append(interval)
        return result