class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for brac in s:
            if brac not in pairs:
                stack.append(brac)
            else:
                if not stack:
                    return False
            
                if stack[-1] != pairs[brac]:
                    return False

                stack.pop()

        return not stack
