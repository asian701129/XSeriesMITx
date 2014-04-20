def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    # check the initial guess to see if it's fine
    if isMyNumber(guess) == 0:
        return guess
    # loop until we've found the number
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        #too small, make the guess bigger
        if sign == -1:
            guess *= 2
        #correct, return that number
        elif sign == 0:
            foundNumber = True
        #too big, make the guess smaller
        else:
            guess -= 1
    #return the number we found
    return guess
