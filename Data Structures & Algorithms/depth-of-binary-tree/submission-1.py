# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxD_r = 1
        maxD_l = 1
        if root.right:
            maxD_r += self.maxDepth(root.right)
             
        if root.left:
            maxD_l += self.maxDepth(root.left)
        return max(maxD_r, maxD_l)
