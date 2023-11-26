# Big O(n) of Linked List:
# Insertions: O(1)
# Delete: O(1)
# Indexing: O(n)

class Node:
    def __init__(self, info):
        self.info = info 
        self.next = None

    # def setNext(self, node):
    #     self.next = node

    # def __repr__(self):
    #     return self.info

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    
    def __iter__(self):
        node = self.head 
        while node is not None:
            yield node
            node = node.next
        self.tail = node

    def size(self):
        size = 0
        if self.head == None:
            return 0
        for node in self:
            size += 1
        return size
    
    #search and return the first occurence of node if found, -1 if node is not existed, not return anything if list is empty 
    def findNode(self, node):
        if self.head == None:
            return
        cur = self.head
        for index in range(0, self.size()):
            if cur.info == node.info:
                return index
            cur = cur.next
        return -1

    def getNodeByIndex(self, index):
        if self.head == None:
            return
        if index >= self.size():
            return
        cur = self.head
        for i in range(0, index):
            cur = cur.next
        return cur

    def insert(self, node):
        if self.head == None:
            self.head = self.tail = node
            return
        for cur in self:
            pass
        cur.next = node 
        self.tail = node
    
    def sortedInsert(self, node):
        if self.head == None:
            self.head = self.tail = node
            return
        cur = self.head
        index = 0
        for cur in self:
            if node.info < cur.info:
                break
            index+=1
        self.addIndex(node, index)
    
    def addFirst(self, node):
        if self.head == None:
            self.head = node
            return
        cur = node
        cur.next = self.head
        self.head = cur

    # Index count from 0, so if addIndex(Node(6), 4) to Linked List [5, 1, 2, 3, 4] -> [5, 1, 2, 3, 6, 4]
    def addIndex(self, node, index):
        if self.head == None:
            self.head = node
            return
        if index > self.size():
            return
        if index == 0:
            self.addFirst(node)
            return
        if index == self.size():  
            self.insert(node)
            return
        cur = self.head
        for i in range(0, index - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def deleteFirst(self):
        if self.head == None:
            return
        self.head = self.head.next

    def deleteLast(self):
        if self.head == None:
            return
        if self.size() == 1:
            self.head = self.tail = None
            return
        cur = self.head
        while True:
            cur = cur.next
            if cur.next.next == None:
                break
        cur.next = None
        self.tail = cur

    def deleteIndex(self, index):
        if self.head == None:
            return
        if index >= self.size():
            return
        if index == self.size() - 1:
            self.deleteLast()
            return
        if index == 0:
            self.deleteFirst()
            return
        cur = prev = self.head
        for i in range(0, index):
            prev = cur
            cur = cur.next
        prev.next = cur.next

    #repr current Linked List
    def __repr__(self) -> str:
        lList = []
        for node in self:
            lList.append(repr(node.info))
        return "[" + ", ".join(lList) + "]"

l = LinkedList()
l.sortedInsert(Node(4))
l.sortedInsert(Node(1))
l.sortedInsert(Node(3))
l.sortedInsert(Node(2))
l.insert(Node(-1))
print(l)