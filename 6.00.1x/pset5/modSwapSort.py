def modSwapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L

myList = [40, 2, 3, 5, 2, 10, 44, 50, 23, 80, 33]
print "My Test List is: ", myList
sortedList = modSwapSort(myList)
print "My List after sort is:", sortedList