class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        s = s.replace(" ", "")
        for ch in range(len(s)):
            if s[ch].isdigit():
                num = num * 10 + int(s[ch])
            if (not s[ch].isdigit()) or ch == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(num * -1)
                elif op == "*":
                    prev = stack.pop()
                    res = prev * num
                    stack.append(res)
                else:
                    prev = stack.pop()
                    res = int(prev/num)
                    stack.append(res)
                num = 0
                op = s[ch]
        return sum(stack)