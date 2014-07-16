# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummy = ListNode(-1)
        p , lastp = head, dummy
        while p != None:
            if p.val < lastp.val:
                lastp = dummy
            pos = self.findPos(lastp, p.val)
            lastp = pos
            tmp = p.next
            p.next = pos.next
            pos.next = p
            p = tmp
        return dummy.next
    
    def findPos(self, head, x):
        pre = head
        p = head.next
        while  p != None and p.val < x:
            pre = p
            p = p.next
        return pre
        