def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # examine linear combinations
    
    # determine the maximum values of a, b, and c
    a_max = n/6
    b_max = n/9
    c_max = n/20

    # configure the search spaces of a, b, and c    
    a_space = range(a_max+1)
    b_space = range(b_max+1)
    c_space = range(c_max+1)

    '''
    # define linear mcnuggets
    a = b = c = 0
    linear_mcnuggets = (6*a + 9*b + 20*c)
    '''
    
    # examine a few simple cases
    if (n % 6 == 0 or n % 9 == 0 or n % 20 == 0):
        # n is directly divisible
        return True
    if (n < 20 and not n == 15):
        # 15 is the only number under 20 that is a comb of 9 and 6
        return False
 
    # the core of the algorithm
   
    #fix 20 fix 9 vary 6
    for c in c_space:
        for b in b_space:
            for a in a_space:
                if (a == b == c == 0):
                    continue
                elif (n % (6*a + 9*b + 20*c) == 0):
                    return True
    #fix 20 fix 6 vary 9
    for c in c_space:
        for a in a_space:
            for b in b_space:
                if (a == b == c == 0):
                    continue
                elif (n % (6*a + 9*b + 20*c) == 0):
                    return True    
    #fix 9 fix 20 vary 6
    for b in b_space:
        for c in c_space:
            for a in a_space:
                if (a == b == c == 0):
                    continue
                elif (n % (6*a + 9*b + 20*c) == 0):
                    return True
    #fix 9 fix 6 vary 20
    for b in b_space:
        for a in a_space:
            for c in c_space:
                if (a == b == c == 0):
                    continue
                elif (n % (6*a + 9*b + 20*c) == 0):
                    return True
    #fix 6 fix 20 vary 9
    for a in a_space:
        for b in b_space:
            for c in c_space:
                if (a == b == c == 0):
                    continue
                elif (n % (6*a + 9*b + 20*c) == 0):
                    return True
    #fix 6 fix 9 vary 20
    for a in a_space:
        for b in b_space:
            for c in c_space:
                if (a == b == c == 0):
                    continue
                if (n % (6*a + 9*b + 20*c) == 0):
                    return True
    return False