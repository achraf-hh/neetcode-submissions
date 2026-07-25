# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(curr):
            if not curr:
                return
            if q.val < curr.val and p.val < curr.val:
                return dfs(curr.left)
            elif q.val > curr.val and p.val > curr.val:
                return dfs(curr.right)
            elif p == curr or q == curr:
                return curr
            return curr
                  
        
        return dfs(root)
