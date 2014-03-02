'''
PROBLEM 1: PAYING THE MINIMUM
'''
def payingMinimum(balance, annualInterestRate, monthlyPaymentRate):

    monthlyInterestRate = annualInterestRate/12.0
    balanceRemaining = balance
    paidTotal = 0
    for currentMonth in range(1,13):
        minimumMonthlyPayment = monthlyPaymentRate * balanceRemaining
        print ('Month: ' + str(currentMonth))
        print ('Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2)))
        balanceRemaining = balanceRemaining - minimumMonthlyPayment
        paidTotal = paidTotal + minimumMonthlyPayment
        balanceRemaining = balanceRemaining * (1.0+monthlyInterestRate)
        print ('Remaining balance: ' + str(round(balanceRemaining,2)))
    print ('Total paid: ' + str(round(paidTotal,2)))
    print ('Remaining balance: ' + str(round(balanceRemaining,2)))
    
#payingMinimum(balance, annualInterestRate, monthlyPaymentRate)
payingMinimum(4213, .20, .04)
payingMinimum(4842, .20, .04)