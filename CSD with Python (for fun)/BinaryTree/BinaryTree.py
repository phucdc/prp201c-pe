class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None

    def insert(self, node):
        if self.isEmpty():
            self.root = node
            return
        f = None
        p = self.root
        while p is not None:
            if node.key == p.key:
                return
            elif node.key > p.key:
                f = p
                p = p.right
            else:
                f = p
                p = p.left
        if node.key > f.key:
            f.right = node
        else:
            f.left = node

    # return Node that have key or None if no Node with required key
    def search(self, key):
        if self.isEmpty():
            return
        cur = self.root
        while cur is not None:
            if cur.key == key:
                return cur
            if key > cur.key:
                cur = cur.right
            else:
                cur = cur.left
        return

    # find height of tree (or sub-tree, with root is a leaf of main tree)
    '''
    Height |       Tree
    1      |         3
           |       /   \
    2      |     2       5
           |    /       / \
    3      |   1       4   6
           |                \
    4      |                 7
        
        => height(root) or height(search(3)) = 4
        => height(search(2)) also can be called as height(root.left) = height(search(6)) = 2
        => height(search(1)) = height(search(4)) = height(search(7)) = 1
        => height(search(5)) also can be called as height(root.right) = 3
    '''
    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
    
    # get the level of a node in tree, for example from bellow, node 5 has level 2 (level(Node(5)) = 2), node 7 has level 4 (level(Node(7)) = 4)
    # if you fill in a Node that not exist (level(Node(10))) then it return None
    def level(self, node):
        if node is None:
            return
        cur = self.root
        lv = 0
        while cur is not None:
            if cur.key == node.key:
                return lv + 1
            if node.key > cur.key:
                cur = cur.right
                lv += 1
            else:
                cur = cur.left
                lv += 1
        return

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.key, end = " ")
            self.inOrder(root.right)
    
    def preOrder(self, root):
        if root:
            print(root.key, end = " ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.key, end = " ")

    # breadth first search or breadth first tranversal or level order tranversal
    def breadthFirstSearch(self):
        cur = self.root
        result = []
        queue = []
        queue.append(cur)
        while len(queue) != 0:
            cur = queue.pop(0)
            result.append(cur.key)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return result
   
    # real nightmare, delete by copying and delete by merging
    def deleteByCopy(self, key):
        p = self.search(key)
        if p is None:
            return
        f = None
        cur = self.root
        # find father of cur (f)
        while p.key != cur.key:
            f = cur
            if cur.key > p.key:
                cur = cur.left
            else: 
                cur = cur.right
        # if p has no child
        if p.left is None and p.right is None:
            if f is None:
                self.root = None
            elif f.left == p:
                f.left = None
            else:
                f.right = None
        # if p has left child only
        elif p.left is not None and p.right is None:
            if f is None:
                root = p.left
            elif f.left == p:
                f.left = p.left
            else:
                f.right = p.left
        # if p has right child only
        elif p.left is not None and p.right is None:
            if f is None:
                root = p.right
            elif f.left == p:
                f.left = p.right
            else:
                f.right = p.right
        # if p has both child
        elif p.left is not None and p.right is not None:
            cur = p.left
            f = None
            # get the lastest right child of left child of p
            while cur.right is not None:
                f = cur
                cur = cur.right
            # delete node p 
            p.key = cur.key
            if f is None:
                p.left = cur.left
            else:
                f.right = cur.left
    
    def deleteByMerging(self, key):
        p = self.search(key)
        if p is None:
            return
        # find f - father of node p
        f = None
        cur = self.root
        while cur.key != p.key:
            f = cur
            if cur.key > p.key:
                cur = cur.left
            else:
                cur = cur.right
        # p has no child
        if p.left is None and p.right is None:
            if f is None:
                self.root = None
            elif f.left == p:
                f.left = None
            else:
                f.right = None
        
        # p has left child only
        if p.left is not None and p.right is None:
            if f is None:
                root = p.left
            elif f.left == p:
                f.left = p.left
            else:
                f.right = p.left

        # p has right child only
        if p.left is None and p.right is not None: 
            if f is None:
                root = p.right
            elif f.left == p:
                f.left = p.right
            else:
                f.right = p.right

        # p has both child
        elif p.left is not None and p.right is not None:
            cur = p.left
            # get the lastest right child of left child of node p
            while cur.right is not None:
                cur = cur.right
            # get the right sub-tree's root of node p
            rp = p.right
            cur.right = rp
            if f is None:
                root = p.left
            elif f.left == p:
                f.left = p.left
            else:
                f.right = p.left
    
    '''
        Convert binary tree to balanced binary tree:
        1. inorder tranversal all nodes, store them to a list, so we get a sorted list in ascending
        2. get the middle element of list we got, make it as root of new tree
        3. recursively do the same as 2. for left and right:
            3.1. Get the middle of left half and make it as left child of the root created in step 2.
            3.2. Get the middle of right half and make it as right child of the root created in step 2.
    '''
    # step 1.

    def toList(self, root, arr):
        if not root:
            return
        self.toList(root.left, arr)
        arr.append(root)
        self.toList(root.right, arr)

    # step 2. and 3.
    def toBalance(self, arr, start, end):
        if start > end:
            return None
        mid = (start+end) // 2
        node = arr[mid]
        node.left = self.toBalance(arr, start, mid-1)
        node.right = self.toBalance(arr, mid+1, end)
        return node

    def balance(self, root):
        arr = []
        # step 1.
        self.toList(root, arr)
        n = len(arr)
        # step 2. and 3.
        return self.toBalance(arr, 0, n-1)

    # rotate left
    def rotateLeft(self, root):
        if root.right is None:
            return root
        p = root.right
        root.right = p.left
        p.left = root
        return p
    
    # rotate right
    def rotateRight(self, root):
        if root.left is None:
            return root
        p = root.left
        root.left = p.right
        p.right = p
        return p

if __name__ == '__main__':
    bt = BinaryTree()
    # insert 
    bt.insert(Node(3))
    bt.insert(Node(2))
    bt.insert(Node(5))
    bt.insert(Node(1))
    bt.insert(Node(4))
    bt.insert(Node(6))
    bt.insert(Node(7))
    
    # Depth first tranversals
    print('In Order: ')
    bt.inOrder(bt.root)
    print('\nPre Order: ')
    bt.preOrder(bt.root)
    print('\nPost Order: ')
    bt.postOrder(bt.root)
    
    # breadth first tranversal
    print('\nBread first tranversal:', *bt.breadthFirstSearch(), sep = " ")
