# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap, ret = [], ListNode(-1)
        for item in lists:
            while item != None:
                heapq.heappush(heap, item.val)
                item = item.next
        p = ret
        while heap:
            p.next = ListNode(heapq.heappop(heap))
            p = p.next
        return ret.next