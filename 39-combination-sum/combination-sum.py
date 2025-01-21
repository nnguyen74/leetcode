class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(remain, comb, current_start):
            if remain == 0:
                result.append(list(comb))
                return
            elif remain < 0:
                return
            else:
                for i, num in enumerate(candidates[current_start:]):
                    comb.append(num)
                    backtrack(remain - num, comb, i + current_start)
                    comb.pop()
        backtrack(target, [], 0)
        return result