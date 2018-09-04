# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 1;
        pointer = head;
        while pointer.next != None:
            count += 1
            pointer = pointer.next
        m = count + 1 - n
        pointer = head
        p = 1
        if count == 1:
            return None
        if m == 1:
            return head.next
        while p!= m-1:
            pointer = pointer.next
            p += 1
        pointer.next = pointer.next.next
        return head
        
