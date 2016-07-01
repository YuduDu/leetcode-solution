# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            while head.next:
                if head.val == "flag":
                    return True
                head.val="flag"
                head = head.next
            return False
        else:
            return False