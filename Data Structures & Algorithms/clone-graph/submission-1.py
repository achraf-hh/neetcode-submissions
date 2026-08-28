"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}

        def dfs(curr):
            if not curr:
                return
            if curr in old_new:
                return old_new[curr]
            old_new[curr] = Node(val = curr.val, neighbors = [])
            for n in curr.neighbors:
                old_new[curr].neighbors.append(dfs(n))
            return old_new[curr]
        return dfs(node)