def payDebtOffYear(balance, annualInterestRate):
    '''
    balance: float -> the outstanding balance on the credit card
    annualInterestRate: float -> annual interest rate as a decimal
    returns: int -> the lowest monthly payment that will pay off all debt in under 1 year
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayment = 10
    updatedBalance = balance
    while True:
        for month in range(1, 13):
            monthlyUnpaidBalance = updatedBalance - monthlyPayment
            updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
        if updatedBalance > 0:
            monthlyPayment += 10
            updatedBalance = balance
        else:
            break
    
    return monthlyPayment

#Test Case
print('Lowest Payment:', payDebtOffYear(3329, 0.2))
print('Lowest Payment:', payDebtOffYear(4773, 0.2))
print('Lowest Payment:', payDebtOffYear(3926, 0.2))
print('Lowest Payment:', payDebtOffYear(141, 0.2))
        

