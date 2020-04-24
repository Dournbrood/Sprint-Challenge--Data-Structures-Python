from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.position = 0

    def append(self, item):
        # If we are at capacity, link the current node to the storage head, and then change the current node to storage head. Then overwrite the value.
        if self.position >= self.capacity:
            self.current = self.current.next
            self.current.value = item
        elif self.position == self.capacity-1:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            self.current.next = self.storage.head
            self.position += 1
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            self.position += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        temp_current = self.storage.head
        temp_position = 0

        while temp_current != None and temp_position < self.capacity:
            list_buffer_contents.append(temp_current.value)
            temp_current = temp_current.next
            temp_position += 1

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
