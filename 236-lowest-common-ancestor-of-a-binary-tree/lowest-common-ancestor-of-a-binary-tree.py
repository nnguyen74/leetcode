# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def findNode(node):
            if not node:
                return False
            left_check = findNode(node.left)
            right_check = findNode(node.right)
            self_check = node == p or node == q
            if left_check + right_check + self_check >= 2:
                self.ans = node
            return self_check or left_check or right_check

        findNode(root)
        
        return self.ans

    
        