class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        stack=[]
        operator=["+","-","*","/"]
        for i in S:
            if i not in operator:
                stack.append(int(i))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if i=="+":
                    stack.append(num2+num1)
                elif i=="-":
                    stack.append(num2-num1)
                elif i=="*":
                    stack.append(num2*num1)
                elif i =="/":
                    stack.append(num2//num1)
        return stack[0]