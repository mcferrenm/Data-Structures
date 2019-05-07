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
        return self.next
    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev
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
        self.max = node if node else None

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            self.head = self.head.insert_before(value)
            self.length += 1

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None

        elif self.head == self.tail:
            current_head = self.head

            self.head = None
            self.tail = None
            self.length = 0

            return current_head.value

        else:
            current_head = self.head
            self.head.delete()
            self.head = self.head.next
            self.length -= 1
            return current_head.value

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            self.tail = self.tail.insert_after(value)
            self.length += 1

    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None

        elif self.head == self.tail:
            current_tail = self.tail

            self.head = None
            self.tail = None
            self.length = 0

            return current_tail.value

        else:
            current_tail = self.tail
            self.tail.delete()
            self.tail = self.tail.prev
            self.length -= 1
            return current_tail.value

    def move_to_front(self, node):
        if not self.head and not self.tail:
            return None

        elif self.head == self.tail:
            pass

        else:
            self.delete(node)

            self.add_to_head(node.value)
            if node == self.tail:
                self.tail = node.prev

    def move_to_end(self, node):
        if not self.head and not self.tail:
            return None

        elif self.head == self.tail:
            pass

        else:
            self.delete(node)
            
            self.add_to_tail(node.value)
            if node == self.head:
                self.head = node.next

    def delete(self, node):
        if not self.head and not self.tail:
            return None

        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0

        else:
            node.delete()
            self.length -= 1

            if node == self.head:
                self.head = node.next
            if node == self.tail:
                self.tail = node.prev

    def get_max(self):
        if not self.head and not self.tail:
            return None
            
        elif self.head == self.tail:
            return self.max.value

        else:
            current_node = self.head

            for _ in range(self.length):
                if current_node.value > self.max.value:
                    self.max = current_node
                current_node = current_node.next

            return self.max.value

