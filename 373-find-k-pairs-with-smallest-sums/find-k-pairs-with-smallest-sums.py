class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i = 0
        j = 0
        result = []
        heap = [(nums1[0] + nums2[1], (0, 0))]
        checked = set()
        checked.add((0, 0))
        while len(result) < k:
            val, (i, j) = heappop(heap)
            print(val, nums1[i], nums2[j])
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in checked:
                heappush(heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                checked.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in checked:
                heappush(heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                checked.add((i, j + 1))
        return result
            
            

        return result
        

                
