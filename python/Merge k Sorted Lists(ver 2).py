# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)
    def mergeLists(self, lists, l , r):
        if l >= r:
            return lists[l]
        else:
            mid = l + ((r - l) >> 1)
            left_list, right_list = self.mergeLists(lists, l, mid), self.mergeLists(lists, mid + 1, r)
            return self.mergeTwoLists(left_list, right_list)
    def mergeTwoLists(self, l1, l2):
        p = ListNode(-1)
        q = p
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1 != None:
            p.next = l1
        else:
            p.next = l2
        return q.next