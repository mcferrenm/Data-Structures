class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass
        if len(self.storage) <= 1:
            self.storage.pop()
        else:
            # current_max = self.storage[0] why do we store the number we are deleting?
            self.storage[0] = self.storage.pop()

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        # loop until either element reaches the top of the array
        # or we'll break the loop when we realize the element's priority
        # is not larger than its parent's value
        while index > 0:
            # the value at 'index' fetches the index of its parent
            parent = (index - 1) // 2  # includes floor
            # check if the element at 'index' has higher priority than
            # the elment at parent index
            if self.storage[index] > self.storage[parent]:
                # then we need to swap the elements
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

            # update the index to move up the tree (parent index)
            else:
                # otherwise, our element has reached a spot in the heap where
                # its parent element has higher priority; stop climbing
                break
            index = parent

    def _sift_down(self, index):
        pass


h = Heap()

# print(h.storage)
h.insert(10)
h.insert(7)
# # h.delete()
print(h.storage)

"""
l = 2i + 1
r = 2i + 2
p = floor((i - 1) / 2)
"""
