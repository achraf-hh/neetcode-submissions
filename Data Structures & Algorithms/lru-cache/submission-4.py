class ListNode:
    def __init__(self, key = 0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy = ListNode(None)
        self.tail = ListNode(None)
        self.tail.prev = self.dummy
        self.dummy.next = self.tail
    
    def _remove(self, node: ListNode) -> None:
        temp = node.prev
        node.prev = None
        node.next.prev = temp
        temp.next = node.next
        node.next = None
    def _insert(self, node: ListNode) -> None:
        temp = self.dummy.next
        self.dummy.next = node
        node.next = temp
        node.prev = self.dummy
        temp.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            node.val = value
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._insert(node)
        if len(self.cache) > self.capacity:
            node = self.tail.prev
            del self.cache[node.key]
            self._remove(node)
        
        
