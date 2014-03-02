'''
PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER
'''

def leftToPay(balanceRemaining, monthlyInterestRate, testPayment):
    for currentMonth in range(1,13):
        #each month
        #pay the minimum you want to pay, owe balanceRemaining
        balanceRemaining = balanceRemaining - testPayment
        #then get charged interest on that remaining amount
        balanceRemaining = balanceRemaining * (1.0+monthlyInterestRate)
    #final balance after 12 months is the leftover
    finalBalance = balanceRemaining
    return finalBalance

def oneYearPayoff(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate/12.0
    balanceRemaining = balance
    print str(monthlyInterestRate)
    lowerBound = balance/12
    print ('Initial Lower: ' + str(lowerBound))
    upperBound = ((balance*(1 + monthlyInterestRate)**12))/12
    print ('Initial Upper: ' + str(upperBound))
    centerValue = lowerBound + (upperBound - lowerBound) /2
    testPayment = centerValue
    print ('Initial Tester: ' + str(testPayment))
    print ''
    
    lowestPayment = 0
    finalBalance = balanceRemaining

    iterationCount = 0
    

    while (finalBalance > 0.03) and (iterationCount < 25):
        #for this given test payment, check how much is left to pay
        print ('Iteration: ' + str(iterationCount))
        print ('Lets try paying: ' + str(testPayment))
        finalBalance = leftToPay(balanceRemaining, monthlyInterestRate, testPayment)
        print ('We still owe: ' + str(finalBalance))
        if (abs(finalBalance) <= 0.10):
            #if we owe less than 10 cents, then our testPayment is good!
            lowestPayment = testPayment
            break
        else:
            #if we owe more than 10 cents, set a new testPayment and go again
            '''finalBalance is not acceptable,
            so we bisect here, and either we need to pay
            more money (right)
            less money (left)
            '''
            iterationCount = iterationCount + 1
            if (finalBalance > 0):
                print ('We need to pay more.')
                lowerBound = centerValue
                centerValue = lowerBound + (upperBound - lowerBound) / 2
            elif (finalBalance < 0):
                print ('We need to pay less.')
                upperBound = centerValue
                centerValue = lowerBound + (upperBound - lowerBound) / 2
            print ''
            testPayment = centerValue
            balanceRemaining = balance
            finalBalance = balanceRemaining


    lowestPayment = testPayment
    print ('Lowest Payment: ' + str(round(lowestPayment,2)))


    
    
#oneYearPayoff(balance, annualInterestRate)
oneYearPayoff(50000000, 0.1)
#oneYearPayoff(999999, 0.18)
