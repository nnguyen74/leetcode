# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(root):
            if root == None:
                return
            print(root.val)
            if len(heap) == k:
                check = heappop(heap)
                if root.val < -check:
                    heappush(heap, -root.val)
                else:
                    heappush(heap, check)
            else:
                heappush(heap, -root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return -heappop(heap)
            