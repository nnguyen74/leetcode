class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            left_arr[i] = left_arr[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            right_arr[i] = right_arr[i + 1] * nums[i + 1]
        return [a * b for a, b in zip(left_arr, right_arr)]