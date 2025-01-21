class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        """
        #Lazy solution
        result = [""]
        digit_list = list(digits)
        for digit in digit_list:
            result = [current_combination + letter for current_combination in result for letter in mappings[digit]]
        return result
        """
        #DFS
        result = []
        def backtrack(index, path):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            letters = mappings[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        backtrack(0, [])
        return result

