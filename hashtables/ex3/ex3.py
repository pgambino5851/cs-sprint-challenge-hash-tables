def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for i in range(0, len(arrays)):
        # print(arrays[i])
        arr = arrays[i]
        for j in range(0, len(arr)):
            key = arr[j]
            # cache[key] = 1
            if key not in cache:
                # print(key)
                cache[key] = 1
            else:
                # print(cache[key])
                cache[key] = cache[key] + 1
            # print(arr[j])
    for i in cache:
        if cache[i] == len(arrays):
            result.append(i)
    # print(cache)
    # print(result)

    return result


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))


result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ])

print(result)