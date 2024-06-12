from estruturas.NodeTree import NodeTree

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return NodeTree(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search_rec(root.left, key)
        else:
            return self._search_rec(root.right, key)
    
    def remove(self, key):
        self.root = self._remove_rec(self.root, key)

    def _remove_rec(self, root, key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = self._remove_rec(root.left, key)
        elif key > root.key:
            root.right = self._remove_rec(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._remove_rec(root.right, temp.key)
        
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, callback):
        self._inorder_rec(self.root, callback)

    def _inorder_rec(self, root, callback):
        if root:
            self._inorder_rec(root.left, callback)
            callback(root.key)
            self._inorder_rec(root.right, callback)