class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            if target == nums[begin]:
                return begin
            if target == nums[end]:
                return end
            if target > nums[end] and target < nums[begin]:
                return -1
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid
            # when to go right
            # if pivot is right side, then go right if target is larger than mid or smaller than end
            # if pivot is left side, then go right if target is larger than mid but smaller than start
            # pivot right side
            if nums[mid] > nums[end]:
                if target > nums[mid] or target < nums[begin]:
                    begin = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] < nums[begin]:
                print("pivot left")
                if target > nums[mid] and target < nums[begin]:
                    begin = mid + 1
                else:
                    end = mid - 1
            #if in order
            elif nums[begin] <= nums[end]:
                if target > nums[mid]:
                    begin = mid + 1
                else:
                    end = mid - 1
        return -1
        
