def isBob(substring):
    '''
    substring: a 3 letter string
    returns: whether or not it equals bob
    '''
    if ('bob' in substring):
        return True

def bobCheck(s):
    '''
    s: a string containing a word
    returns: whether or not it equals bob
    '''
    count = 0
    for i in range(len(s)):
        if (isBob(s[i:i+3])):
            count = count + 1
    return count

#print "Number of vowels: " + str(bobCheck(s))
#print "Number of BOBS: " + str(bobCheck(s))
print "Number of times bob occurs is: " + str(bobCheck(s))
