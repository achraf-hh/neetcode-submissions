# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        dia = 0

        def dfs(curr):
            nonlocal dia
            if not curr:
                return 0
            l, r = dfs(curr.left), dfs(curr.right)
            dia = max(dia, l+r)
            return 1 + max(l, r)
        dfs(root)
        return dia
            