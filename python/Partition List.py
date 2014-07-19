# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        left_dummy, right_dummy = ListNode(-1), ListNode(-1)
        left_p, right_p = left_dummy, right_dummy
        p = head
        while p != None:
            if p.val < x:
                left_p.next = p
                p = p.next
                left_p = left_p.next
            else:
                right_p.next = p
                p = p.next
                right_p = right_p.next
        left_p.next = right_dummy.next
        right_p.next = None
        return left_dummy.next
                