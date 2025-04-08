from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxStack = deque()
        result = [-1] * len(nums) * 2
        num_double = nums + nums
        for i, num in enumerate(num_double[::-1]):
            numCheck = -1
            while maxStack:
                if num >= maxStack[-1]:
                    maxStack.pop()
                else:
                    numCheck = maxStack[-1]
                    break
            maxStack.append(num)
            result[i] = numCheck
        return result[::-1][:len(nums)]
                    