# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs_check(node, low=-math.inf, high=math.inf):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return dfs_check(node.right, node.val, high) and dfs_check(node.left, low, node.val)
        return dfs_check(root)