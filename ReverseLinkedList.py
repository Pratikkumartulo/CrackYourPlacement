# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        ptr = head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head):
            while(ptr):
                nextnd = ptr.next
                ptr.next = prev
                prev = ptr
                ptr=nextnd
            return prev
        else:
            return head
        