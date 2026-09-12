"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map2clone = defaultdict(Node)

        def dfs(curr):
            if not curr:
                return 
            if curr not in map2clone:
                map2clone[curr] = Node(curr.val, [])
                for nei in curr.neighbors:
                    map2clone[curr].neighbors.append(dfs(nei))
                else:
                    return map2clone[curr]

            return map2clone[curr]
        return dfs(node)