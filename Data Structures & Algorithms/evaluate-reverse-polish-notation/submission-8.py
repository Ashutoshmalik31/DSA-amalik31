class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in ["+", "-", "/", "*"]:
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()

                if tok == "+":
                    stack.append(a + b)
                elif tok == "*":
                    stack.append(a * b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "/":
                    stack.append(int(a/b))
        return stack[0]    
    
       
        # stack = []
        # for token in tokens:
        #     if token not in {"+", "-", "*", "/"}:
        #         stack.append(int(token))
        #     else:
        #         b = stack.pop()
        #         a = stack.pop()

        #         if token == "+":
        #             stack.append(a + b)
        #         elif token == "-":
        #             stack.append(a - b)
        #         elif token == "*":
        #             stack.append(a * b)
        #         else:
        #             stack.append(int(a / b)) 

        # return stack[0]
        