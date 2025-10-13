class ListNode:
    def __init__(self, val=0, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveNodeToFront(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            newNode = ListNode(val=value, key=key)
            self.cache[key] = newNode
            self.addNode(self.cache[key])
        else:
            node = self.cache[key]
            node.val = value
            self.moveNodeToFront(node)
        if len(self.cache.keys()) > self.capacity:
            self.removeLastNode()

    def addNode(self, node):
        frontNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = frontNode
        frontNode.prev = node

    def moveNodeToFront(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode

        self.addNode(node)

    def removeLastNode(self):
        lastNode = self.tail.prev
        key = lastNode.key
        del self.cache[key]
        newLastNode = lastNode.prev
        newLastNode.next = self.tail
        self.tail.prev = newLastNode

# 1 2 3 4
# 1 3 4 2

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)