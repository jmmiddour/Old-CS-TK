# A single linked list is kind of shaped like a list, but nothing has an index list

class Node:  # Create the node class
    def __init__(self, value):  # Instantiates the class with value attribute
        self.value = value  # Define the attribute value
        self.next = None  # Create a next attribute with a None value.

    def get_value(self):  # Define a method to get the value
        return self.value  # Return the value


class LinkedList:
    def __init__(self):
        self.head = None  # Points to the first node (head)
        self.tail = None  # Points to the last node (tail)

    def add_to_tail(self, value):  # Add new value to the end of the linked list
        new_node = Node(value)  # Creates a new node and allocates space for node and pointer

        if self.head is None:  # Check if there is anything in the first node, if None:
            self.head = new_node  # New node is both head...
            self.tail = new_node  # and tail because there is only one node.
            return  # Stops the code.

        self.tail.next = new_node  # Points the current pointer for the tail to new node.
        self.tail = new_node  # Adds the value and null pointer for the new tail.

    def add_to_head(self, value):  # Adds new value as the head node and points to old head.
        new_node = Node(value)  # Creates a new node and allocates the space for node and pointer.

        if self.head is None:  # Check to see if there is already a head node, if None:
            self.head = new_node  # New node is both head...
            self.tail = new_node  # and tail because there is only one node.
            return
        old_head = self.head  # Creates a pointer to original head value, to keep track of it,
        self.head = new_node  # Makes the new node value and pointer the new head node.
        self.head.next = old_head  # Pointer for new head points to old head.
    
    def remove_head(self):  # Removes the head node value and pointer and reassigns the head to next node.
        if self.head is None:  # Check if there is anything in the head, if None...
            return  # End function, nothing to remove.

        data = self.head.get_value()  # Store the head node's value

        if self.head.next is None:  # Check if the head pointer is pointing to another node, if None...
            self.head = None  # We are removing the only value in the list, no more head value.
            self.tail = None  # Have no tail value either because the list is now empty.
            return data  # Return the stored value that was in the head to reuse.

        self.head = self.head.next  # If there are still values, need to reassign the head to the next node.
        return data  # Return the stored value that was in the head to reuse if needed.

    def remove_tail(self):  # Removes the tail node value and null pointer and reassigns the tail to the prior node.
        if self.head is None:  # Check if there is a head node, if None...
            return  # End program, nothing to remove.

        cursor = self.head  # Empty pointer that starts at the head to iterate through the list to find tail.
        data = self.tail.get_value()  # Stores the value of the current tail for later use.

        if self.head.next is None:  # Check if the head is pointing to anything, if None...
            self.head = None  # These is only one value (the head) so head is now None.
            self.tail = None  # There is no tail, because head and tail are the same value.
            return data  # Returns the value of the original tail for later use.

        # Iterates through the list until it finds the tail by moving to the next node's pointer, looking for None.
        while cursor.next.next is not None:
            cursor = cursor.next  # Moves the pointer to the next node until it is at the node before the tail.

        self.tail = cursor  # Assigns the tail to the cursor position, which is the node just before the original tail.
        self.tail.next = None  # Assigns the new tail's pointer to None.
        return data  # Returns the original tail's value to reuse.


# x = Node(15)  # Run test on code

# print(x)  # Prints just the memory location of the node.

# print(x.value)  # Prints the value of the node.

# print(x.next.value)  # Prints the next value if there is one. Will throw error if value is None
