class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        mod_seen = {0 : - 1}
        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
        return False
        
            
        
        