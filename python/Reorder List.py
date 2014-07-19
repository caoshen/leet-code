# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        p, q = head, head
        while q and q.next:
            p = p.next
            q = q.next.next
        head_r = p
        if p == None:
            return head
        else:
            pre, cur, tmp = p, p.next, None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            head_r.next = None
            p1, p2 = head, pre
            while p1 != head_r:
                t1, t2 = p1.next, p2.next
                p1.next = p2
                p2.next = t1
                p1, p2 = t1, t2
            p1.next = None
            return head