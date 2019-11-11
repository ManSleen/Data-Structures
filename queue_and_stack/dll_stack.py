from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList(None)

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.tail is not None:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
