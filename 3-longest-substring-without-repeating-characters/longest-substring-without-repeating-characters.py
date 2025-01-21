class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word_dict = dict()
        lastDupe = -1
        maxLength = 0
        for i, char in enumerate(s):
            if char in word_dict:
                lastDupe = max(lastDupe, word_dict[char])
            word_dict[char] = i
            maxLength = max(maxLength, i - lastDupe)
        return maxLength