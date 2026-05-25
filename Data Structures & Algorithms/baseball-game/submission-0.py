class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                total = int(stack[-1]) + int(stack[-2])
                stack.append(total) 
            elif op == "C":
                stack.pop()
            elif op == "D":
                prod = int(stack[-1]) * 2
                stack.append(prod) 
            else:
                stack.append(int(op))
        return sum(stack)
        