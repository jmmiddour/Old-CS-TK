class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


# The hashing function does the hashing. You input a string, it outputs a number.
# A hash table using the hash function to take the key of a key value pair and
#   hashes it into an index.

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Potential size of the hash table
        self.storage = [None] * capacity  # Creates the storage buckets
        self.items = 0  # We will start at 0 and count them as we add them


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        """
        An instance of HashMap has two parameters that affect its performance: 
            initial capacity and load factor. The capacity is the number of 
            buckets in the hash table, and the initial capacity is simply the 
            capacity at the time the hash table is created. The load factor is 
            a measure of how full the hash table is allowed to get before its 
            capacity is automatically increased. When the number of entries in 
            the hash table exceeds the product of the load factor and the 
            current capacity, the hash table is rehashed (that is, internal data 
            structures are rebuilt) so that the hash table has approximately 
            twice the number of buckets.

        As a general rule, the default load factor (.75) offers a good tradeoff 
            between time and space costs. Higher values decrease the space 
            overhead but increase the lookup cost (reflected in most of the 
            operations of the HashMap class, including get and put). The 
            expected number of entries in the map and its load factor should 
            be taken into account when setting its initial capacity, so as to 
            minimize the number of rehash operations. If the initial capacity 
            is greater than the maximum number of entries divided by the load 
            factor, no rehash operations will ever occur.

        """
        return (self.items / self.capacity)



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # algorithm fnv-1 :
        #     hash := FNV_offset_basis
        #     for each byte_of_data to be hashed do
        #         hash := hash × FNV_prime
        #         hash := hash XOR byte_of_data
        # return hash

        FNV_prime = 1099511628211
        FNV_offset = 14695981039346656037

        hash=FNV_offset
        for char in key:
            hash *= FNV_prime
            hash ^= ord(char)  # Bitwise XOR

        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        # Ava's Code
        hash_prime = 5381

        for byte in key:
            hash_prime = (hash_prime * 33) + ord(byte)

        return hash_prime


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Josh's code
        # index = self.hash_index(key)
        # node = HashTableEntry(key, value)
        #
        # if self.storage[index] is not None:
        #
        #     if self.storage[index].key == key
        #         self.storage[index].value = value
        #
        #     else:
        #         current = self.storage[index]
        #
        #         while current.next is not None:
        #             if current.key == key:
        #                 current.value = value
        #
        #             else:
        #                 current = current.next
        #
        #         if current.key == key:
        #             current.value = value
        #
        #         else:
        #             current.next = node
        #             self.size += 1
        #
        # else:
        #     self.storage[index] = node
        #     self.size += 1

        # Ava's code
        index = self.hash_index(key)
        new_entry = HashTableEntry(key, value)  # Creates a new node

        if self.storage[index] is not None:
            if self.storage[index].key == key
                self.storage[index].value = value

            else:
                current = self.storage[index]

            while current.next is not None:
                if current.key == key:
                    current.value = value

                current = current.next

                if current.key == key:
                    current.value = value

                else:
                    current.next = new_entry

        else:
            self.storage[index] = new_entry

        self.items += 1

        if self.get_load_factor() >= 7:
            self.resize((self.capacity * 2))


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # # Ava's code (1st Evening Session
        # index = self.hash_index(key)
        #
        # if self.storage[index] is None:
        #     return None
        #
        # elif self.storage[index].key == key:
        #     self.items -= 1
        #
        #     if self.storage[index].next is not None:
        #         self.storage[index] = self.storage[index].next
        #
        #     else:
        #         self.storage[index] = None
        #
        # else:
        #     prev = self.storage[index]
        #     current = self.storage[index].next
        #
        #     while current is not None:
        #
        #         if current.key == key:
        #             prev.next = current.next
        #             self.items -= 1
        #
        #         else:
        #             prev = current
        #             current = current.next
        #
        # return 'Success!'


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # Ava's code
        index = self.hash_index(key)

        if self.storage[index] is None:
            return None

        elif self.storage[index].key == key:
            return self.storage[index].value

        elif self.storage[index] is not None:
            current = self.storage[index]

            while current.next is not None:
                next_node = current.next

                if next_node.key == key:
                    return next_node.value

                else:
                    current = next_node

            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        # Ava's code
        old_table = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for entry in old_table:
            if entry is not None:
                self.put(entry.key, entry.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
