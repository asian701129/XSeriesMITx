def probn(n):
    '''
    n: (int) n > 0 number of rolls of a die
    returns: the probability that it takes n rolls to get a given face of a die
    '''
    # n = 1, then 1/6 chance to get your face
    # n = 2, then (5/6) chance of another face times (1/6) chance of your face
    return (1.0/6.0)*(5.0/6.0)**(n-1)
    
def probTest(limit):
    '''
    limit: the highest probabilty limit
    currentprob: the prob of observing on nth trial
    '''
    n = 1
    currentprob = (1.0/6.0)
    while not (currentprob < limit):
        n += 1
        currentprob = probn(n)
    return n
    
    
print probn(1)
print probn(2)
print probn(3)
print probn(4)
print probTest(0.01)
