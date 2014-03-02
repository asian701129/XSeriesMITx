'''
PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER
'''

def leftToPay(balanceRemaining, monthlyInterestRate, testPayment):
    for currentMonth in range(1,13):            
        balanceRemaining = balanceRemaining - testPayment
        balanceRemaining = balanceRemaining * (1.0+monthlyInterestRate)
        print ('Month: ' + str(currentMonth))
        print ('Remaining balance: ' + str(round(balanceRemaining,2)))
    finalBalance = balanceRemaining
    return finalBalance

def oneYearPayoff(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate/12.0
    balanceRemaining = balance
    
    lowerBound = balanceRemaining/12
    upperBound = (balanceRemaining*(1+monthlyInterestRate)**2)/12
    centerValue = (upperBound - lowerBound) /2
    testPayment = centerValue
    
    lowestPayment = 0
    finalBalance = balanceRemaining

    loopcount = 0
    

    while (finalBalance - 0) > 0.03 and loopcount < 10:    
        #for this given test payment, check how much is left to pay
        finalBalance = leftToPay(balanceRemaining, monthlyInterestRate, testPayment)
        if (finalBalance == 0):
            #if we owe exacatly 0 dollars, then our testPayment is good!
            lowestPayment = testPayment
        elif (finalBalance - 0) > 0.03:
            #if we are more than 3 cents off, set a new testPayment and go again
            '''
            finalBalance is not acceptable, so we bisect here,
            either we need to pay more money (right)
            or we overpaid (left)
            '''
            if (finalBalance - 0) > 0.03:
                print 'We owe more than 3 cents remaining'
                lowerBound = centerValue
          	centerValue = lowerBound + (upperBound - lowerBound) / 2
            elif (-finalBalance - 0) < -0.03:
                print 'We overpaid more than 3 cents'
                upperBound = centerValue
       	        centerValue = upperBound + (upperBound - lowerBound) / 2
        testPayment = centerValue
        balanceRemaining = balance


    lowestPayment = testPayment
    print ('Lowest Payment: ' + str(round(lowestPayment,2)))
    


    '''
    this next section of code from problem 2 needs to be re-written
    '''
    
    '''
    while finalBalance > 0:

        for currentMonth in range(1,13):            
            balanceRemaining = balanceRemaining - testPayment
            paidTotal = paidTotal + testPayment
            balanceRemaining = balanceRemaining * (1.0+monthlyInterestRate)
            print ('Month: ' + str(currentMonth))
            print ('Remaining balance: ' + str(round(balanceRemaining,2)))

        finalBalance = balanceRemaining
	if (finalBalance >=1):
	    testPayment = testPayment + 10
	    balanceRemaining = balance


    lowestPayment = testPayment
    print ('Lowest Payment: ' + str(round(lowestPayment,2)))
    '''
    
    
#oneYearPayoff(balance, annualInterestRate)
oneYearPayoff(3329, 0.2)
oneYearPayoff(4773, 0.2)