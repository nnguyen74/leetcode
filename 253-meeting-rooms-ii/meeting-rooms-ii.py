from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        rooms = []
        max_room = 0
        for interval in intervals:
            start, end = interval[0], interval[1]
            while len(rooms) > 0:
                end_room, start_room = heappop(rooms)
                if end_room > start:
                    heappush(rooms, (end_room, start_room))
                    break
            heappush(rooms, (end, start))
            max_room = max(max_room, len(rooms))
        return max_room




