def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in range(0, len(a)):
        key = a[i]
        cache[key] = 1

    for key in cache:
        if key > 0:
            if (key * -1) in cache:
                result.append(key)
    # print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

