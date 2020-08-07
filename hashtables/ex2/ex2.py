#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    for i in range(length):
        table[tickets[i].source] = tickets[i].destination
    route = [None]*length
    following = ""
    for i in range(length):
        if i == 0:
            following = table["NONE"]
            route[i] = following
            following = table[following]
        else:
            route[i] = following
            following = table[following]
    return route
