class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+","-","*","/"]
        for e in tokens:
            if e in operations and stack:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                res = 0
                if e == "+":
                    res = val1 + val2
                elif e == "-":
                    res = val1 - val2
                elif e == "*":
                    res = val1 * val2
                else:
                    res = val1 / val2
                stack.append(res)
            else:
                stack.append(e)
        return int(stack[-1])