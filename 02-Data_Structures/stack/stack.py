import os
import sys

# sys.path.append(os.path.join(os.path.dirname(sys.path[0]),
#                              'singly_linked_list'))
sys.path.insert(2, '/singly_linked_list')

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

########## Doing it with List ##########
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         # choose only one option below, does not matter if you add to head or tail whenn stacking, just need to be consistant.
#         self.storage.append(value) # Adds to tail.
#         # self.storage.insert(0, value) # Adds to the head.

#     def pop(self):
#         if len(self.storage) == 0:
#             return
#         # removed = self.storage[0]
#         # del self.storage[0]
#         removed = self.storage[-1]
#         del self.storage[-1]
#         return removed

########## Doing it with Link List ##########
# import sys, os
# sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
# from singly_linked_list import LinkedList


# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0  #
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_head()