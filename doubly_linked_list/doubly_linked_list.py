"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        pass

    def remove_from_head(self):
        # remove_from_head removes the head node and returns the value stored in it.
        # 1. What if our linked list is empty?
        if not self.head and not self.tail:
            return None
        # 2. What if our linked list has 1 node?
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        # 3. What if our linked list has 2 or more nodes?
        else:
            self.head = self.head.next
            self.head.delete()
            self.length -= 1

    def add_to_tail(self, value):
        # add_to_tail replaces the tail of the list with a new value that is passed in
        new_node = ListNode(value)
        # 1. What is our linked list is empty?
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # 2. What if our linked list is not empty?
        else:
            self.tail.insert_after(new_node)
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass

# remove_from_tail removes the tail node and returns the value stored in it.
# move_to_front takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down.
# move_to_end takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up.
# delete takes a reference to a node in the list and removes it from the list. The deleted node's previous and next pointers should point to each afterwards.
# get_max returns the maximum value in the list.


ll = DoublyLinkedList()

ll.add_to_tail(5)
ll.remove_from_head()
print(ll.__len__())
