# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = []
        while head:
            if head.val not in s:
                s.append(head.val)
            head = head.next
        
        new = None
        while len(s)!=0:
            node = ListNode(s.pop())
            node.next = new
            new = node
        
        return new