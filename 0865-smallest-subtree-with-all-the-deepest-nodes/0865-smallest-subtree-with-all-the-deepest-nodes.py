# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # Returns (depth, LCA of deepest nodes in this subtree)
            if not node:
                return (0, None)
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            # If left subtree is deeper, deepest nodes are all on the left
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            # If right subtree is deeper, deepest nodes are all on the right
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            # If both subtrees have same depth, current node is the LCA
            else:
                return (left_depth + 1, node)
        
        return dfs(root)[1]
            
        
        