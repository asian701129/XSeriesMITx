'''
PROBLEM 2: PAYING DEBT OFF IN A YEAR
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
    balanceRemaining, finalBalance = balance, balance
    testPayment = 0
    lowestPayment = 0

    iterationCount = 0
	
    while (finalBalance > 0):
        finalBalance = leftToPay(balanceRemaining, monthlyInterestRate, testPayment)
        if (finalBalance > 0):
            testPayment = testPayment + 10
            balanceRemaining = balance
            iterationCount = iterationCount + 1
            
    lowestPayment = testPayment
    print ('Total Iterations: ' + str(iterationCount))
    print ('Lowest Payment: ' + str(round(lowestPayment,2)))
    
#oneYearPayoff(balance, annualInterestRate)
oneYearPayoff(3329, 0.2)
#oneYearPayoff(4773, 0.2)

