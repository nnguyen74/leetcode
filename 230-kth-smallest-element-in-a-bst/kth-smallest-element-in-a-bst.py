# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_list = []
        found = False
        k_smallest = -1
        def dfs(root):
            nonlocal found
            nonlocal k_smallest
            if root == None or found:
                return
            dfs(root.left)
            node_list.append(root.val)
            if len(node_list) == k:
                found = True
                k_smallest = root.val
                return
            dfs(root.right)
        dfs(root)
        return k_smallest
            