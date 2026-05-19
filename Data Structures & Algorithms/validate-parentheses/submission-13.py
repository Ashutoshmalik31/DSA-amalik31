class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        res = []
        for c in s:
            if c in valid_pair:
                if res and res[-1] == valid_pair[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return res == []

        # valid_pair = {
        #     "}": "{",
        #     "]": "[",
        #     ")": "("
        # }
        # stack = []
        # for paran in s:
        #     if paran in valid_pair:
        #         if stack and valid_pair[paran] == stack[-1]:
        #             stack.pop()
        #         else:
        #             return False        
        #     else:
        #         stack.append(paran)
        # return stack == []
