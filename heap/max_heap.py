class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):

        if not len(self.storage):
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            current_max = self.storage[0]
            self.storage[0] = self.storage.pop()

            self._sift_down(0)

            return current_max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

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
        while index < len(self.storage) - 1:

            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child <= len(self.storage) - 1 and right_child <= len(self.storage) - 1:
                if self.storage[left_child] > self.storage[right_child]:
                    if self.storage[index] < self.storage[left_child]:
                        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
                else:
                    if self.storage[index] < self.storage[right_child]:
                        self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
            elif left_child <= len(self.storage) - 1:
                if self.storage[index] < self.storage[left_child]:
                    self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
            index += 1


h = Heap()

h.insert(6)
h.insert(7)
h.insert(5)
h.insert(8)
h.insert(10)
h.insert(1)
h.insert(2)
h.insert(5)


# print(h.get_size())
# print(h.delete())

descending_order = []

while h.get_size() > 0:
    descending_order.append(h.delete())

"""
l = 2i + 1
r = 2i + 2
p = floor((i - 1) / 2)
"""
