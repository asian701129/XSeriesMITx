def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

def newersearch(L, e):
    size = len(L)
    for i in range(size):
        dummy = size-i-1
        if L[dummy] == e:
            return True
        if L[i] < e:
            return False
    return False



myList = [2, 2, 3, 5, 10, 23, 33, 40, 44, 50, 80]
lookForThis = 50
print "My Test List is: ", myList, "and I am looking for", lookForThis
foundOrNot = search(myList, lookForThis)
print "Original Gives:", foundOrNot
foundOrNot = newersearch(myList, lookForThis)
print "New Search Gives:", foundOrNot