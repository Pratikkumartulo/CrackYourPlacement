class node:
    def __init__(self):
        self.data = None
        self.next = None
class Solution:
    def multiply_two_lists(self, first, second):
        MOD = 10**9 + 7
        
        def list_to_number(node):
            num = 0
            while node:
                num = (num * 10 + node.data) % MOD
                node = node.next
            return num
        
        num1 = list_to_number(first)
        num2 = list_to_number(second)
        result = (num1 * num2) % MOD
        
        return result