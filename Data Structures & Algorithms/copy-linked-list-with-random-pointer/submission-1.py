"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map2copy = {}
        if not head:
            return None

        def rec(curr):
            if not curr:
                return None
            if curr in map2copy:
                return map2copy[curr]
            else:
                copy = Node(curr.val)
                map2copy[curr] = copy
                ran, ne = rec(curr.random) , rec(curr.next)
                copy.next = ne
                copy.random = ran

            return map2copy[curr]
        return rec(head)


