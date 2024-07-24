# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ptr=head.next
        nxt=head
        while(ptr!=None):
            while(ptr!=None and ptr.val==nxt.val):
                ptr=ptr.next
            nxt.next=ptr
            nxt=ptr
        return head
    
'''
Here , I have added 2 pointer ptr and nxt and the ptr just move step by step while it is same as ptr==nxt and and as soon as it finds a different
value the nxt pointer get pointed to the ptr pointer.
'''