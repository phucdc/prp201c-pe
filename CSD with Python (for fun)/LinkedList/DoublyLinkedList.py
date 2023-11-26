class Node:
    def __init__(self, info):
        self.info = info
        self.prev = self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def getIndex(self, node):
        cur = self.head
        index = 0
        while cur is not None:
            if cur.info == node.info:
                return index
            index += 1
            cur = cur.next
        return -1

    def addFirst(self, node):
        self.size += 1
        if self.isEmpty():
            self.head = self.tail = node
            return
        cur = node
        cur.next = self.head
        self.head.prev = node
        self.head = node

    def addLast(self, node):
        self.size += 1
        if self.isEmpty():
            self.head = self.tail = None
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        node.prev = cur
        cur.next = node
        self.tail = node

    def addIndex(self, node, index):
        if self.isEmpty():
            self.head = self.tail = None
            self.size += 1
            return
        if index > self.size or index < 0:
            return
        elif index == self.size:
            self.addLast(node)
        elif index == 0:
            self.addFirst(node)
        else:
            cur = self.head
            for i in range(0, index - 1):
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next = node
        self.size += 1

    def deleteFirst(self):
        if self.isEmpty():
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
    
    def deleteLast(self):
        if self.isEmpty():
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def deleteIndex(self, index):
        if self.isEmpty() or index < 0 or index > self.size - 1:
            return
        if index == 0:
            self.deleteFirst()
        elif index == self.size - 1:
            self.deleteLast()
        else:
            cur = self.head
            for i in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1

    def __repr__(self) -> str:
        cur = self.head
        dl = []
        while cur is not None:
            dl.append(repr(cur.info))
            cur = cur.next
        return '[' + ', '.join(dl) + ']'

if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.addFirst(Node(1))
    dl.addFirst(Node(2))
    dl.addLast(Node(3))
    dl.addLast(Node(6))
    dl.addIndex(Node(4), 1)
    print(dl)
    dl.deleteIndex(2)
    print(dl)
    print(dl.size)