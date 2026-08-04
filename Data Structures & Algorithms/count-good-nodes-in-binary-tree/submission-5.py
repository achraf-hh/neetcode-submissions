# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, max_val):
            nonlocal res
            maxi = max_val
            if not curr:
                return 
            if curr.val >= maxi:
                res += 1
                maxi = curr.val
            dfs(curr.left, maxi)
            dfs(curr.right, maxi)
            return curr.val
        dfs(root, root.val)
        return res


            
                


