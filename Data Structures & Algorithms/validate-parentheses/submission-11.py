class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for paran in s:
            if paran in valid_pair:
                if stack and valid_pair[paran] == stack[-1]:
                    stack.pop()
                else:
                    return False        
            else:
                stack.append(paran)
        return stack == []
