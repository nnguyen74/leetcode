class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alphabet_check = [0] * 26
        for char in p:
            alphabet_check[ord(char) - ord('a')] += 1
        start = 0
        end = len(p)
        result = []
        current_window = [0] * 26
        for char in s[start:end]:
            current_window[ord(char) - ord('a')] += 1
        if current_window == alphabet_check:
            result.append(start)
        while end < len(s):
            current_window[ord(s[start]) - ord('a')] -= 1
            start += 1
            end += 1
            current_window[ord(s[end - 1]) - ord('a')] += 1
            if current_window == alphabet_check:
                result.append(start)
        return result
            
            