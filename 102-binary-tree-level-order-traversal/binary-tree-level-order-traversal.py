# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return empty case
        if not root:
            return []
        #Initialize result node and queue
        result = []
        nodes = deque()
        nodes.append((root, 0))
        while nodes:
            # Each entry contrains a node and the level
            node, level = nodes.popleft()
            # Add child node and increased level to queue
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
            # If first node in the level
            if len(result) < level + 1:
                result.append([node.val])
            # If there already exists result in that level
            else:
                result[level].append(node.val)
        return result