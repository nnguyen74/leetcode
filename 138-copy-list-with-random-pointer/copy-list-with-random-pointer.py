"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visitedHash = {}
        def cloneNode(head):
            if head == None:
                return None
            if head in visitedHash:
                return visitedHash[head]
            node = Node(head.val)
            visitedHash[head] = node
            node.next = cloneNode(head.next)
            node.random = cloneNode(head.random)
            return node
        return cloneNode(head)

        
