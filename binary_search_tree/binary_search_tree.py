import random


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
        if not self.value:
            return False
        elif target == self.value:
            return True
        else:
            if target > self.value:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False
            else:
                if self.left:
                    return self.left.contains(target)
                else:
                    return False

    def get_max(self):
        if not self.right and not self.left:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        if not self.value:
            pass
        else:
            cb(self.value)

            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)
