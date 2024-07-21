class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def apply_op(op, b, a):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a / b) 

        def to_postfix(expression):
            stack = []
            postfix = []
            num = ""
            
            for ch in expression:
                if ch.isdigit():
                    num += ch
                else:
                    if num:
                        postfix.append(num)
                        num = ""
                    if ch == ' ':
                        continue
                    if ch == '(':
                        stack.append(ch)
                    elif ch == ')':
                        while stack and stack[-1] != '(':
                            postfix.append(stack.pop())
                        stack.pop()
                    else: 
                        while stack and precedence(stack[-1]) >= precedence(ch):
                            postfix.append(stack.pop())
                        stack.append(ch)
            
            if num:
                postfix.append(num)
                
            while stack:
                postfix.append(stack.pop())

            return postfix

        def evaluate_postfix(postfix):
            stack = []
            for token in postfix:
                if token.isdigit():
                    stack.append(int(token))
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(apply_op(token, b, a))
            return stack[0]
        postfix = to_postfix(s)
        return evaluate_postfix(postfix)