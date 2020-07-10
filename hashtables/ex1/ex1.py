def get_indices_of_item_weights(weights, length, limit):

    cache = {}
    for i in range(0, len(weights)):
        key = i
        cache[key] = weights[i]
    
    answerArr = None
    print(cache)
    keyList = list(cache.keys())
    valList = list(cache.values())
    print(keyList)
    print(valList)
    # print(valList)
    for j in range(0, len(weights)):
        complement = limit - weights[j]
        # print(complement)
        if complement in cache.values():
            # print(complement)
            print(keyList[valList.index(complement)])
            print(keyList[valList.index(weights[j])])
            answerArr = [keyList[valList.index(complement)], (keyList[valList.index(weights[j])])]
            # answer = (cache[weights[j]], cache[complement])
            # print(answer)
    print(answerArr)
    if answerArr is not None:
        answerArr.sort()
        return (answerArr[1], answerArr[0])
    else:
        return None

    
    """
    YOUR CODE HERE
    """
    # Your code here

    return None

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)
