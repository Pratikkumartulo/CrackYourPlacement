# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ptr=head
        num=0
        while(ptr!=None):
            num=(num*10)+ptr.val
            ptr=ptr.next
        num=int(str(num),2)
        return num
'''
First we traverse the whole linked list then, making an integer using the numbers, then we use the pre defined function in python, to convert 
the string to integer
'''