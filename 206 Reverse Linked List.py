# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        if head==None:
            return head
        
        while head:
            node = ListNode(head.val)
            node.next = new_head
            new_head = node
            head = head.next
        return new_head
        