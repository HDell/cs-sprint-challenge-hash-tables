def get_indices_of_item_weights(weights, length, limit): #(list of ints, int, int)
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    counter = 0
    for weight in weights:
        table[weight] = (counter, limit - weight)
        counter += 1
    
    counter = 0

    for weight in weights:
        if (limit - weight) in table.keys():
            if table[limit - weight][0] > table[weight][0]:
                return (table[limit - weight][0] , table[weight][0])
            elif table[limit - weight][0] < table[weight][0]:
                return (table[weight][0], table[limit - weight][0])
            else: # table[limit - weight][0] == table[weight][0]
                for i in range (length):
                    if (weights[i] == (limit - weight)) and i < table[limit - weight][0]:
                        return (table[limit - weight][0], i)

    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
print(get_indices_of_item_weights([0, 4], 2, 8))