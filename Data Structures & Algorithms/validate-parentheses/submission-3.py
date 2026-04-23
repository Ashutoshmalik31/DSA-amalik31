class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        if len(s) > 1:
            res = []
            for char in s:
                if char in valid_pair:
                    res.append(char)
                else:
                    if res:
                        if char == valid_pair.get(res[-1]):
                                res.pop()
                        else:
                            res.append(char)
                    else:
                        res.append(char)
            if res:
                return False
            else:
                return True
        else:
            return False