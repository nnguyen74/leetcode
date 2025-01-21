
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            neg_squared_distance = -(x ** 2 + y ** 2)
            if len(heap) < k:
                heapq.heappush(heap, (neg_squared_distance, i))
            else:
                if neg_squared_distance > heap[0][0]:
                    heapq.heappushpop(heap, (neg_squared_distance, i))
        return [points[i] for (_, i) in heap]
        