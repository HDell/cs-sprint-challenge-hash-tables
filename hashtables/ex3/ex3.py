def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    table = {}
    for array in arrays:
        for elem in array:
            if elem in table.keys():
                table[elem] += 1
            else:
                table[elem] = 1
    for item in table.items():
        if item[1] == len(arrays):
            result.append(item[0])
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
