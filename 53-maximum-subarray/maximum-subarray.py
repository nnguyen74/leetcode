class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -inf
        currentSum = 0
        for i, num in enumerate(nums):
            if currentSum + num <= 0:
                maxSum = max(currentSum + num, maxSum) #handle edge case where first number is negat
                currentSum = 0
            else:
                currentSum += num
                maxSum = max(currentSum, maxSum)
        return maxSum