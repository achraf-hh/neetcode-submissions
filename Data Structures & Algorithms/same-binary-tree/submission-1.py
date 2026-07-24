# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q and p and q.val != p.val:
            return False
        if not q and not p:
            return True
        if (not q and p) or (q and not p):
            return False
        return self.isSameTree(q.left, p.left) and self.isSameTree(p.right, q.right)
        