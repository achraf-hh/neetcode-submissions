# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        curr = head
        hist = []
        while curr:
            if curr.next in hist:
                return True
            hist.append(curr)
            curr = curr.next
        return False
        