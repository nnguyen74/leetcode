class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = max(piles)
        while left < right:
            middle = (left + right) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / middle)
            if hour <= h:
                right = middle
            else:
                left = middle + 1
        return right
        


        

