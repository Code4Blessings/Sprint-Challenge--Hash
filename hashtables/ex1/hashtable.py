class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.total = 0  # Number of elements in hash table
        self.capacity = capacity
        self.storage = [None] * capacity

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        #Found here: http://www.cse.yorku.ca/~oz/hash.html
        hash_value = 5381
        for c in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(c)
        return hash_value & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        self.djb2(key)
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        new_node = HashTableEntry(key, value)
        index = self.hash_index(key)
        # Search the list for the key
        # If it's there, replace the value
        if self.storage[index] == None:
            self.storage[index] = new_node
        # If it's not, append a new record to the list
        elif self.storage[index].key == key:
            self.storage[index].value = value
            #In any other case where the keys do not match, but there is a node present, you have to add the current node to the new_node's next property
        else:
            new_node.next = self.storage[index]
            self.storage[index] = new_node

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        #Check to see if the node exists at that index
        if node is not None:
            #check to see if the keys match, then return its value
            if node.key == key:
                return node.value
        #If there is a node but the keys don't match, then loop through all of its next properties until you find the right key
            else:
                current_node = node.next
                while current_node is not None:
                    if current_node.key == key:
                        return current_node.value
                    current_node = current_node.next
                    # If the key does not exist after looping, then return None
        else:
            return None
