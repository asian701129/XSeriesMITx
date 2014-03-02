'''
PROBLEM 2: PAYING DEBT OFF IN A YEAR
'''
def oneYearPayoff(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate/12.0
    balanceRemaining = balance
    testPayment = 0
    lowestPayment = 0
    paidTotal = 0
    finalBalance = balanceRemaining


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
    
oneYearPayoff(balance, annualInterestRate)
#oneYearPayoff(3329, 0.2)
#oneYearPayoff(4773, 0.2)