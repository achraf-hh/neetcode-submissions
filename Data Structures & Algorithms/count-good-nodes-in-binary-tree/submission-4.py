# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque([(root, root.val)])
        while queue:
            node, curr_max = queue.popleft()
            if node.val >= curr_max:
                res+=1
                curr_max = node.val
            if node.left:
                queue.append((node.left, curr_max))
            if node.right:
                queue.append((node.right, curr_max))
        return res
            
                


