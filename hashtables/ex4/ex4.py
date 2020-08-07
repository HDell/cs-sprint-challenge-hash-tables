def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    result = []

    for num in a:
        if num > 0 and num not in table.keys():
            table[num] = (num * -1, 1)
        elif num > 0 and num in table.keys():
            table[num] = (num * -1, table[num][1] + 1)
    
    for num in a:
        if num < 0 and ((num * -1) in table.keys()):
            if table[(num * -1)][1] == 1:
                result.append(num * -1)
            elif table[(num * -1)][1] > 1:
                result.append(num * -1)
                table[(num * -1)] = (num, table[(num * -1)][1] - table[(num * -1)][1])
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
