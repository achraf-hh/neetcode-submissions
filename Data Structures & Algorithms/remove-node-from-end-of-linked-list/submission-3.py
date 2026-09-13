# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        nodesMap = defaultdict(ListNode)
        curr = head
        c = 0
        while curr:
            nodesMap[c] = curr
            c += 1
            curr = curr.next
        m = len(nodesMap)
        if n == len(nodesMap):
            temp = head.next
            head.next = None
            return temp
        temp = nodesMap[m-n].next
        nodesMap[m-n].next = None
        nodesMap[m-n-1].next = temp
        return head

