# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        if head == None or k == 0:
            return head
        p = head
        while k != 0:
            k -= 1
            p = p.next
            if p == None:
                p = head
        if p == None:
            return head
        q = head
        while p.next != None:
            p = p.next
            q = q.next
        p.next = dummy.next
        dummy.next = q.next
        q.next = None
        
        return dummy.next
        
        
