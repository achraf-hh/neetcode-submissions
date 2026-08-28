"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new = {}
        q = deque()
        q.append(node)
        old_new[node] = Node(val = 1, neighbors = [])
        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in old_new:
                    old_new[n] = Node(val = n.val, neighbors = [])
                    q.append(n)
                old_new[curr].neighbors.append(old_new[n])
        return old_new[node]