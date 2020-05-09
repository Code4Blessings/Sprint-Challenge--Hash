# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# Hash int
def hash(x, max):
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)

    return x % max


def hash_table_insert(hash_table, key, value):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is not None:
        current_pair.value = value
    else:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair


def hash_table_remove(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = last_pair.next

    if current_pair is None:
        print("ERROR: Unable to remove entry with key " + key)
    else:
        if last_pair is None:  # Removing the first element in the LL
            hash_table.storage[index] = current_pair.next
        else:
            last_pair.next = current_pair.next


def hash_table_retrieve(hash_table, key):
    index = hash(key, len(hash_table.storage))

    current_pair = hash_table.storage[index]

    while current_pair is not None:
        if(current_pair.key == key):
            return current_pair.value
        current_pair = current_pair.next
