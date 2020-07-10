# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in range(0, len(files)):
        key = files[i]
        cache[key] = key.split('/')
    print(cache)
    # for j in range(0, len(queries)):
    # print(cache.values())


    for j in range(0, len(queries)):
        for key in cache.keys():
            if queries[j] in cache[key]:
                result.append(key)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
            "qux"
        ]
    print(finder(files, queries))