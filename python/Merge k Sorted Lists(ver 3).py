# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        n = len(lists)
        if n == 0:
            return None
        stride, a, b = 1, 0, 1
        while stride < n:
            lists[a] = self.mergeTwoLists(lists[a], lists[b])
            a = b + stride
            b = a + stride
            if a >= n or b >= n:
                stride <<= 1
                a, b = 0, stride
        return lists[0]
    def mergeTwoLists(self, p, q):
        dummy = ListNode(-1)
        r = dummy
        while p != None and q != None :
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next
        if q != None:
            r.next = q
        else:
            r.next = p
        return dummy.next