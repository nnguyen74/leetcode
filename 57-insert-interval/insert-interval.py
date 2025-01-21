class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        check_interval_start = newInterval[0]
        check_interval_end = newInterval[1]
        merged = False
        for i, interval in enumerate(intervals):
            interval_start = interval[0]
            interval_end = interval[1]
            # Case 1: interval to the left of check interval
            if interval_end < check_interval_start:
                result.append(interval)
            # Case 2: interval to the right of check interval
            elif interval_start > check_interval_end:
                # Handle case where the new interval has no ovelap
                if not merged:
                    result.append(newInterval)
                    merged = True
                result.extend(intervals[i:])
                break
            # Case 3: interval has overlap
            else:
                # Check if a merge has happened
                if merged:
                    result.pop()
                check_interval_start = min(interval_start, check_interval_start)
                check_interval_end = max(interval_end, check_interval_end)
                result.append([check_interval_start, check_interval_end])
                merged = True
        # If all intervals are smaller than new interval
        if not merged:
            result.append(newInterval)
        return list(result)