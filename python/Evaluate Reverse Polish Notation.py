class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    a += b
                elif i == '-':
                    a -= b
                elif i == '*':
                    a *= b
                else:
                    a = float(a) / b
                    a = int(a)
                stack.append(a)
        return stack[0]
