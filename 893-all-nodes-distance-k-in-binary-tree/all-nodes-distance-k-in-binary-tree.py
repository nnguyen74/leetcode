# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_child_dict = {root: None}
        def iterate_tree(root):
            if not root:
                return
            if root.left != None:
                parent_child_dict[root.left] = root
                iterate_tree(root.left)
            if root.right != None:
                parent_child_dict[root.right] = root
                iterate_tree(root.right)
        iterate_tree(root)
        node_layer = [target]
        visited = set(node_layer)
        for i in range(k):
            new_layer = set()
            for node in node_layer:
                for neighbor in (node.left, node.right, parent_child_dict[node]):
                    if neighbor and neighbor not in visited:
                        new_layer.add(neighbor)
                        visited.add(neighbor)
            node_layer = new_layer
        return [node.val for node in node_layer]



