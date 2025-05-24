"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = set()
        node_dict = dict()
        queue = deque()
        queue.append(node)
        node_dict[node.val] = Node(node.val)
        while queue:
            old_node = queue.popleft()
            neighbors = old_node.neighbors
            new_node = node_dict[old_node.val]
            for neighbor in neighbors:
                if neighbor.val not in node_dict:
                    queue.append(neighbor)
                    node_dict[neighbor.val] = Node(neighbor.val)
                new_node.neighbors.append(node_dict[neighbor.val])
        return node_dict[node.val]




        