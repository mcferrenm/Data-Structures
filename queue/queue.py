class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.size += 1
        return self.storage.add_to_tail(item)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

    def len(self):
        return self.size

# a linked list data structure
# node class
# self.value self.next, get value, get next value, set next value (set value with constructor)
# linkedlist class
# self.head self.tail,


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new node
        new_node = Node(value)

        # 1. What if our linked list is empty?
        # 1a. How do we check if it is empty?
        if not self.head and not self.tail:
            # if our list is empty, then the node that we add to
            # the list needs to be set as both the head and the tail
            self.head = new_node
            self.tail = new_node
        # 2. What if our linked list is not empty?
        else:
            # add to the tail of the list
            # update the previous tail node's next_node reference to point to the new node
            self.tail.set_next(new_node)
            # update the linked list's self.tail reference to the new tail node
            self.tail = new_node

    def remove_head(self):
        # 1. what if our linked list is empty?
        if not self.head and not self.tail:
            return None
        # 2. what if our linked list has one node?
        # if not self.head.get_next():
        elif self.head == self.tail:
            old_head = self.head
            # now set both and tail to none (final result of removing the only node)
            self.head = None
            self.tail = None
            return old_head.get_value()
        # 3. what if our linke dlist has more than one node?
        else:
            # set the list's head reference to the head node's next node
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.get_value()

    def contain(self, value):
        # make sure list is not empty
        if not self.head and not self.head:
            return None

        current = self.head
        # keep traversing while we are at a valid node / we are pointing at None
        while current:
            if current.get_value() == value:
                return True
                # update our current pointer
            current = current.get_next()
        # we've gone through the enitre list and we haven't found it return false
        return False


q = Queue()

# q.enqueue(100)
# q.enqueue(101)
q.enqueue(105)
q.dequeue()
q.len()
q.dequeue()


print(q.len())
