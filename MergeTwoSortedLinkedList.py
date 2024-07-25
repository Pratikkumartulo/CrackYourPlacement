# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1=list1
        ptr2=list2
        result=ListNode()
        ptr3=result
        while(ptr1 is not None and ptr2 is not None):
            if ptr1.val<ptr2.val:
                ptr3.next=ptr1
                ptr1=ptr1.next
            else:
                ptr3.next=ptr2
                ptr2=ptr2.next
            ptr3=ptr3.next
        while ptr1 is not None:
            ptr3.next=ptr1
            ptr3=ptr3.next
            ptr1=ptr1.next
        while ptr2 is not None:
            ptr3.next=ptr2
            ptr3=ptr3.next
            ptr2=ptr2.next
        ptr3=None
        return result.next