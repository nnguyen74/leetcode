class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        leftIndex = []
        s = list(s)
        #Removing extra closing bracket
        for index, char in enumerate(s):
            if char == ")":
                if balance <= 0:
                    s[index] = "_"
                else:
                    balance -= 1
            elif char == "(":
                balance += 1
                leftIndex.append(index)
        #If more opening bracket, remove extra opening bracket from the right
        if balance > 0:
            for index in leftIndex[-1: -(balance + 1): -1]:
                s[index] = "_"
        return ''.join(s).replace("_", "")