# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        curr = head
        visit.add(head)
        while curr:
            if curr.next in visit:
                return True
            else:
                curr = curr.next
                visit.add(curr)
        return False