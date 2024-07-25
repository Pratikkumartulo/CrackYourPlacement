# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        head = l3
        carry=0
        while(l1 and l2):
            value = l1.val+l2.val+carry
            carry = value//10
            l3.next = ListNode(value%10)
            l3=l3.next
            l1=l1.next
            l2=l2.next
        while(l1):
            value = l1.val+carry
            carry = value//10
            l3.next = ListNode(value%10)
            l3=l3.next
            l1=l1.next
        while(l2):
            value =l2.val+carry
            carry = value//10
            l3.next = ListNode(value%10)
            l3=l3.next
            l2=l2.next
        if carry:
            l3.next = ListNode(carry)
        return head.next
        
            
        
        
        