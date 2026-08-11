# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True

        def dfs(curr):
            nonlocal isBal
            if not curr:
                return 0
            lh, rh = dfs(curr.left), dfs(curr.right)
            if (rh-lh)**2 > 1:
                isBal = False
            return 1 + max(rh, lh)
        dfs(root)
        return isBal
            