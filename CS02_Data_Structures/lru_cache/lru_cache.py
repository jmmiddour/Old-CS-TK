from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit  # max number of nodes
        self.current = 0  # current number of spaces taken in the cache
        self.cache = None  # this will become the doubly linked list on the first set()
        self.storage = {}  # this would be another Data Structure that would store the encryption for the key and probably encryption

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:

            pointer = self.cache.head
            while pointer is not None:
                if pointer.value == key:
                    break

                else:
                    pointer = pointer.next

            self.cache.move_to_front(pointer)
            return self.storage[key]

        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            self.storage[key] = value  # overwrites key with new value
            pointer = self.cache.head

            while pointer is not None:
                if pointer.value == key:
                    break

                else:
                    pointer = pointer.next

            self.cache.move_to_front(pointer)
        else:
            if self.current == 0:
                self.cache = DoublyLinnkedList(ListNode(key))
                self.storage[key] = value
                self.current += 1

            elif self.current == self.limit:
                removed_key = self.cache.remove_from_tail()
                del self.storage[removed_key]
                self.cache.add_to_head(key)
                self.storage[key] = value

            else:
                self.cache.add_to_head(key)
                self.storage[key] = value
                self.current += 1