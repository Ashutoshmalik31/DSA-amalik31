class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cachemap = {}
        self.cap = capacity

        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, Node):
        prev, nxt = Node.prev, Node.next
        prev.next, nxt.prev = nxt, prev 
    
    def insert(self, Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = Node
        Node.next, Node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cachemap:
            self.remove(self.cachemap[key])
            self.insert(self.cachemap[key])
            return self.cachemap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cachemap:
            self.remove(self.cachemap[key])
        self.cachemap[key] = ListNode(key, value)
        self.insert(self.cachemap[key])

        if len(self.cachemap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cachemap[lru.key]

