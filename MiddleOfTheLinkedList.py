# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        mid = head
        while ptr != None and ptr.next != None:
            mid = mid.next
            ptr = ptr.next.next
        return mid
'''
problem me 2 pointer lena and then pehela pointer ko do do ke step me move krna jab ki dusra wala pointer only ek ek place hi move kr rha hoga.
'''