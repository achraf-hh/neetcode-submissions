# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {v:i for i, v in enumerate(inorder)}
        idx = 0
        def build(lo, hi):
            nonlocal idx
            if lo > hi:
                return None
            val = preorder[idx]
            idx += 1
            mid = indices.get(val)
            root = TreeNode(val)
            root.left = build(lo, mid-1)
            root.right = build(mid+1, hi)
            return root
        return build(0, len(inorder)-1)




        
        