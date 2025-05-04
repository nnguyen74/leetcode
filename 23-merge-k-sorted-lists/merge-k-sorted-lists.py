# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode(-1)
        curr = result
        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))
        while heap:
            head_value, list_index, head = heappop(heap)
            curr.next = head
            curr = curr.next
            next_node = head.next
            if next_node:
                heappush(heap, (next_node.val, list_index, next_node))
        return result.next