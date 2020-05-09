from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)

def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    # Set the capacity to 21
    ht = HashTable(21)
    # for the first weight in the range from 0 to length
    for i in range(0, length):  # index
        # insert hashtable, [weight key], and weight value
        hash_table_insert(ht, weights[i], i)
    # for the second weight in the range from 0 to length
    for j in range(0, length):
        # subtract [j] from limit and assign result to limit_weight
        limit_weight = limit - weights[j]
        # retrieve the matching wight from the hash table and assign to match_weight
        match_weight = hash_table_retrieve(ht, limit_weight)
        # if we found a weight ...
        if match_weight:
            # return the match weight and the other weight value
            return (match_weight, j)
    # return None (means no matching weight was found)
    return None
    

