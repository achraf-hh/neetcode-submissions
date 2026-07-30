# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        def dfs(curr, min_val, max_val):
            nonlocal isValid
            if not curr:
                return 
            if curr.val >= max_val:
                isValid = False
            if curr.val <= min_val:
                isValid = False
            
            dfs(curr.left, min_val, curr.val)
            dfs(curr.right, curr.val, max_val)
            return curr.val
        dfs(root, float('-inf'), float('inf'))
        return isValid

                