def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """

    #Create a dictionary and print all of the indices 
    weight_dict = dict()
    #Need to loop through all the values in the length of the dictionary and return 2 indices whose value equals the limit
    for i in range(0, length):
        for weight_1 in range(0, length):  # index
            (weights[weight_1], weight_1)
    # for the second weight in the range from 0 to length
    for weight_2 in range(0, length):
        # subtract [weight value] from limit and assign result to matching_weight
        matching_weight = limit - weights[weight_2]
        # The matching weight and assign to found_weight
           return None

