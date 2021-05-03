def payDebtOffYear(balance, annualInterestRate):
    '''
    balance: float -> the outstanding balance on the credit card
    annualInterestRate: float -> annual interest rate as a decimal
    returns: int -> the lowest monthly payment that will pay off all debt in under 1 year
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayLow = round(balance / 12, 2)
    monthlyPayUp = round((balance * (1 + monthlyInterestRate)**12) / 12.0, 2)
    monthlyPayment = round((monthlyPayLow + monthlyPayUp) / 2, 2)
    updatedBalance = balance
    epsilon = 0.01

    while True:
        for month in range(1, 13):
            monthlyUnpaidBalance = round(updatedBalance - monthlyPayment,2)
            updatedBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance),2)
        
        if updatedBalance > 0 and updatedBalance - monthlyUnpaidBalance > epsilon:
            monthlyPayLow = monthlyPayment        
            updatedBalance = balance
        elif updatedBalance < 0 and updatedBalance - monthlyUnpaidBalance < epsilon:
            monthlyPayUp = monthlyPayment
            updatedBalance = balance
        else:
            break
        
        monthlyPayment = round((monthlyPayLow + monthlyPayUp) / 2, 2)
    
    return monthlyPayment





# Test Case
print('Lowest Payment:', payDebtOffYear(320000, 0.2))
print('Lowest Payment:', payDebtOffYear(999999, 0.18))
print('Lowest Payment:', payDebtOffYear(276996, 0.2))
