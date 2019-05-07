class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # is the value greater?
        if value > self.value:
            # is there already a self.right tree?
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            # is there already a self.left tree?
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass


bst = BinarySearchTree(10)
