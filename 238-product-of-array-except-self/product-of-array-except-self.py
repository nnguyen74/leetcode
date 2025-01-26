class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = [0] * len(nums)
        rightArr = [0] * len(nums)
        leftArr[0] = 1
        for i in range(1, len(nums)):
            leftArr[i] = nums[i - 1] * leftArr[i - 1]
        rightArr[-1] = 1
        for i in reversed(range(len(nums) - 1)):
            rightArr[i] = nums[i + 1] * rightArr[i + 1]
        output = [0] * len(nums)    
        for i in range(len(nums)):
            output[i] = leftArr[i] * rightArr[i]
        return output