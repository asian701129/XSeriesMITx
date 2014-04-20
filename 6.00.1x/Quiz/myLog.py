def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if x == b:
        return 1
    elif x > b:
        #compute the nth powers of b until we are higher than x
        bToN = 0
        n = 0
        while (bToN <= x) and not(n > x):
            n = n + 1
            bToN = b**n
        return n - 1
    elif x < b:
        #compute the nth roots of b until we get x?
        return 0
# Test Cases

# Glass Box Testing
# x = b

# log_2(2) = 1
a =  myLog(2,2)
print "test1 done"
print a
# log_3(3) = 1
a = myLog(3,3)
print "test2 done"
print a
# x > b

# log_2(1) = 4
a = myLog(16,2)
print "test3 done"
print a

# log_3(15) = 2
a = myLog(15,3)
print "test4 done"
print a

# x < b
