'''
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None) ## new List
        t = dummy
        temp1, temp2 = l1,l2
        c = 0
        while temp1 and temp2:

            val = temp1.val + temp2.val + c
            d1 = val % 10
            c = val // 10
            New = ListNode(d1)
            t.next = New
            t = New
            temp1 = temp1.next
            temp2 = temp2.next
        
        while temp1:
            val = temp1.val + c
            d1 = val % 10
            c = val // 10
            New = ListNode(d1)
            t.next = New
            t = New
            temp1 = temp1.next
        
        while temp2:
            val = temp2.val + c
            d1 = val % 10
            c = val // 10
            New = ListNode(d1)
            t.next = New
            t = New
            temp2 = temp2.next
        
        if c != 0:
            New = ListNode(c)
            t.next = New
            t = New
        
        return dummy.next





