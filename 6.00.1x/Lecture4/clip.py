def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    rvalue = lo + hi + x - min(lo, x) - max(x, hi)
    return rvalue

    '''
    this is using conditionals    
    if (x == min(lo,x)):
        return lo
    elif (x == max(x,hi)):
        return hi
    else:
        return x
    '''
       
    
    
    '''
    tony's code v1
    rvalue = lo + hi + x
    rvalue = (rvalue - min(lo, x))
    rvalue = (rvalue - max(x, hi))
    return rvalue
    '''