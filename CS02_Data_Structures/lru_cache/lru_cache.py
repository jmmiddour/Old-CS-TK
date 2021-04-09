from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Least Recently Used (LRU)
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit  # max number of nodes
        self.current = 0  # current number of spaces taken in the cache
        # This is form Ava's Code
        # self.cache = None  # this will become the doubly linked list on the
        #   first set()
        self.cache = DoublyLinkedList()  # Christopher's cache
        self.storage = {}  # this would be another Data Structure that would
    # store the encryption for the key and probably encryption

	"""
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Ava's code from the evening session #
        # if key in self.storage:  # If the key is already in the storage
        #     pointer = self.cache.head  # pointer to point at the head
        #     while pointer is not None:  # As long as there is something at
        #         # the pointer
        #         if pointer.value == key:  # If the pointer value is the
        #         key...
        #             break  # Stop running the code
        #
        #         else:
        #             pointer = pointer.next  # Assign the pointer to point at
        #             # the next node
        #
        #     self.cache.move_to_front(pointer)  # Move the node that the
        #     # pointer is currently pointing at to the front (head) of the
        #     # linked list
        #     return self.storage[key]  # Returns the value in the storage at
        #     # the key
        #
        # else:  # If the key is not in the storage we did not find it.
        #     return None

        if key in self.storage:
            temp_node = self.storage[key]
            print(temp_node)
            self.cache.move_to_front(temp_node)
            return temp_node.value

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
        # Ava's code from the evening session #
        # if key in self.storage:  # Check if the key is already in storage
        #     self.storage[key] = value  # overwrites key with new value
        #     pointer = self.cache.head  # Set the pointer to point to the head
        #     # to add to the beginning of the cache
        #
        #     while pointer is not None:  # While the pointer is not
        #     pointing at
        #         # None and we still have not found the key
        #         if pointer.value == key:  # If the pointer is the key,
        #             # nothing more to do
        #             break  # We are done!
        #
        #         else:
        #             pointer = pointer.next  # Go to the next node to find the
        #             # key we are looking for.
        #
        #     self.cache.move_to_front(pointer)  # Use the move to front method
        #     # in our doubly linked list class
        #
        # else:  # If key not already in the storage
        #     if self.current == 0:  # If nothing in current
        #     # if not self.cache:
        #         self.cache = DoublyLinkedList(ListNode(key))  # Create a node
        #     # for the current and initialize as a doubly linked list
        #         self.storage[key] = value  # adds the value to the storage at
        #     # the key
        #         self.current += 1  # Incrementing the current which is
        #     # keeping track of the number of elements currently in the cache
        #
        #     elif self.current == self.limit:  # When the current is the same
        #         # as the limit
        #         removed_key = self.cache.remove_from_tail()  # Remove the
        #         # tail because that is the oldest value accessed
        #         del self.storage[removed_key]  # This is where we actually
        #         # remove the tail from the linked list
        #         self.cache.add_to_head(key)  # Now we can add the most
        #         # recently used to the head of the linked list
        #         self.storage[key] = value  # Add the value to the storage at
        #         # the key
        #
        #     else:  # If none of the above conditions are met...
        #         self.cache.add_to_head(key)  # Adding the key to the head of
        #         # the linked list
        #         self.storage[key] = value  # Adds the value to the storage at
        #         # the key
        #         self.current += 1  # Increment the current which is keeping
        #         # track of the number of elements currently in the cache.

        # Christopher and I pair-programmed on this code in morning session #
        if key in self.storage:  # Check if the key is already in storage
            temp_node = self.storage[key]  # Creates a new node in the linked list
            # = temp_node  # overwrites key with new value
            temp_node.value = value
            self.cache.move_to_front(temp_node)  # Use the move to front method
            #   in our doubly linked list class to move the temp node to the
            #   front of the linked list

        else:  # If key not already in the storage
            if self.current == self.limit:  # When the current is the same
                # as the limit
                removed_val = self.cache.remove_from_tail()  # Remove the
                # tail because that is the oldest value accessed
                self.current -= 1

                for k, v in self.storage.items():
                    if v.value == removed_val:
                        del self.storage[k]  # This is where we actually
                        # remove the tail from the linked list
                        break

            temp_node = self.cache.add_to_head(value)
            # Now we can add the most
            # recently used to the head of the linked list
            self.storage[key] = temp_node  # Add the value to the storage at
            # the key
            self.current += 1

            # print(temp_node.value, self.cache.print())
