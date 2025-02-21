# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        global p_found, q_found, lca
        p_found = False
        q_found = False
        lca = None

        def findNode(root, p, q):
            global p_found, q_found, lca
            if not root or lca:
                return False
            self_check = False
            if root.val == p.val:
                p_found = True
                self_check = True
            if root.val == q.val:
                q_found = True
                self_check = True
            if p_found and q_found:
                return True
            left_check = findNode(root.left, p, q)
            right_check = findNode(root.right, p, q)
            if (left_check and right_check) or (self_check and left_check) or (self_check and right_check):
                lca = root
            return self_check or left_check or right_check

        findNode(root, p, q)
        
        return lca

    
        