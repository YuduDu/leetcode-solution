# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head==None) or (head.next==None) :
            return head
        
        tN= self.swapPairs(head.next.next)
        tH=head
        head = head.next
        head.next = tH
        head.next.next=tN
        return head
        