class Solution:
    def isValid(self, s: str) -> bool:
        sign_stack = []
        corresponding_symbol = {")": "(", "]": "[", "}": "{"}
        for symbol in s:
            if symbol in {"(", "{", "["}:
                sign_stack.append(symbol)
            else:
                if not sign_stack:
                    return False
                top_stack_symbol = sign_stack.pop()
                if top_stack_symbol != corresponding_symbol[symbol]:
                    return False
        return False if sign_stack else True
