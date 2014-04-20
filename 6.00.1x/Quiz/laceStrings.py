def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    s3 = ''
    stemp = ''
    if len(s1) > len(s2):
        #loop through s2 then tack on rest of s1
        for i in range(len(s2)):
            stemp += s1[i]
            stemp += s2[i]
            s3 += stemp
            stemp = ''
        s3 += s1[len(s2):]
    elif len(s1) < len(s2):
        #loop through s1 then tack on rest of s2
        for i in range(len(s1)):
            stemp += s1[i]
            stemp += s2[i]
            s3 += stemp
            stemp = ''
        s3 += s2[len(s1):]
    else:
        #s1 and s2 are equal in length
        for i in range(len(s2)):
            stemp += s1[i]
            stemp += s2[i]
            s3 += stemp
            stemp = ''
    return s3