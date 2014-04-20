def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if aDict == {}:
        return None
    longest = aDict.keys()[0]
    longestlength = 0
    for key in aDict.keys():
        if len(aDict[key]) > longestlength:
            longest = key
            longestlength = len(aDict[key])
    return longest