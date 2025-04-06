from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)
        result = ''
        while pq:
            count, char = heappop(pq)
            if len(result) == 0 or result[-1] != char:
                result += char
                if count != -1:
                    heappush(pq, (count + 1, char))
            else:
                if not pq:
                    return ""
                count2, char2 = heappop(pq)
                result += char2
                if count2 != -1:
                    heappush(pq, (count2 + 1, char2))
                heappush(pq, (count, char))
        return result
        

        
