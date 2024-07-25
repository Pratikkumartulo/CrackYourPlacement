# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy=ListNode(next=head)
        ptr=dummy
        while ptr.next is not None:
            if ptr.next.val==val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return dummy.next
    
'''
Here we have created another dummy linked list that points to the head and a pointer ptr that traverse the linked list and if the node with
val got find then we remove it from the linked list and at last we return the head of linked list that is dummy.next

'''