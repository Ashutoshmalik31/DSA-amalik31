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
        return True if stack == [] else False


















        # valid_pair = {
        #     "{": "}",
        #     "[": "]",
        #     "(": ")"
        # }
        # if len(s) > 1:
        #     res = []
        #     for char in s:
        #         if char in valid_pair:
        #             res.append(char)
        #         else:
        #             if res:
        #                 if char == valid_pair.get(res[-1]):
        #                         res.pop()
        #                 else:
        #                     return False
        #             else:
        #                 return False
        #     if not res:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False
        valid_pair = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        res = []
        for char in s:
            if char in valid_pair:
                if res and res[-1] == valid_pair.get(char):
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        
        return True if not res else False  