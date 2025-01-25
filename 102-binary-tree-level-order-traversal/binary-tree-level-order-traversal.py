# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        nodes = deque()
        nodes.append((root, 0))
        while nodes:
            node, level = nodes.popleft()
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
            if len(result) < level + 1:
                result.append([node.val])
            else:
                result[level].append(node.val)
        return result