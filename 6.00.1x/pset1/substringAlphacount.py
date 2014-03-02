def NextOrdered(string, j, current):
    '''
    string: the part of the string not yet traversed
    returns: the string in alphabetical order which begins at the current place
    '''
    returnthis = string[0]
    for i in range(len(string)-1):
        if (string[i + 1] >= string[i]):
            returnthis = returnthis + string[i+1]
        else:
            break
    return returnthis
    '''
    if (j == (len(string)-3)):
        return current
    if (string[j+1] >= string[j]):
        print ('iteration'+ str(j))
        current = current + str(j+1)
        current = current + NextOrdered(string[j+1],j+1,current)
    else:
        return current
    '''

def alphacheck(s):
    '''
    s: a string containing a word
    returns: the longest substring in alphabetical order
    '''
    longestsofar = ''
    current = ''
    
    for i in range(len(s)):
        current = NextOrdered(s[i:],i,current)
        if (len(current) > len(longestsofar)):
            longestsofar = current
    return longestsofar

s = 'teststringgoesinhere'
print "Longest substring in alphabetical order is: " + str(alphacheck(s))
