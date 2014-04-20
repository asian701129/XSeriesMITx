def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    print start.myName()
    previous = start.getBefore()
    if previous == None:
        return start
    else:
        return findFront(previous)
        
def findBack(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the ending of the linked list 
    """
    print start.myName()
    subsequent = start.getAfter()
    if subsequent == None:
        return start
    else:
        return findFront(subsequent)
        