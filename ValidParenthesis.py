class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if len(stack) == 0:
                    return False
                else:
                    a = stack.pop()
                    if (a == "(" and i != ")") or (a == "{" and i != "}") or (a == "[" and i != "]"):
                        return False

        return len(stack) == 0