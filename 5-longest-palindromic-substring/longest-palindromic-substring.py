class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        if (s == None or len(s) < 1):
            return ""
        for i in range(len(s)):
            higherLen = max(self.expandAroundCenter(s, i, i), self.expandAroundCenter(s, i, i + 1))
            if (higherLen > (end - start + 1)):
                start = i - ((higherLen - 1) //2)
                end = i + higherLen // 2
        return s[start:end + 1]
    
    def expandAroundCenter(self, s:str, l:int, r:int) -> int:
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            r += 1
            l -= 1
        return r - l - 1