from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        result = ''
        for _ in range(len(s)):
            if len(counter) == 1:
                letter, count = counter.most_common(1)[0]
                if count == 1:
                    return result + letter
                else:
                    return ""
            top_2_common_letters = counter.most_common(2)
            if len(result) != 0 and result[-1] == top_2_common_letters[0][0]:
                letter = top_2_common_letters[1][0]
            else:
                letter = top_2_common_letters[0][0]
            result += letter
            counter[letter] -= 1
            if counter[letter] == 0:
                del counter[letter]
        return result

        
