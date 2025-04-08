# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        if root is None:
            return []
        answer = []
        while True:
            next_level = deque()
            while queue:
                curr = queue.popleft()
                if not queue:
                    answer.append(curr.val)
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            if not next_level:
                break
            queue = next_level
        return answer
                

        