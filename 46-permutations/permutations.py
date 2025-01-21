class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(current, used):
            if len(current) == len(nums):
                answer.append(current.copy())
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                current.append(num)
                used[i] = True
                backtrack(current, used)
                current.pop()
                used[i] = False
        backtrack([], [False] * len(nums))
        return answer