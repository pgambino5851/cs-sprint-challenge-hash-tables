#  Hint:  You may not need all of these.  Remove the unused functions.
import random
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    for i in range(0, length):
        key = tickets[i].source
        cache[key] = tickets[i].destination

    # Your code here
    print(cache)
    result = []
    startingPoint = cache["NONE"]
    result.append(startingPoint)
    nextLink = cache[startingPoint]
    # print(startingPoint)
    # print(nextLink)
    # nextLink = cache[nextLink]
    # print(nextLink)
    # nextLink = cache[nextLink]
    # print(nextLink)
    while nextLink != "NONE":
        print(nextLink)
        result.append(nextLink)
        nextLink = cache[nextLink]
    result.append("NONE")
    print(result)
        
    

    return result

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)