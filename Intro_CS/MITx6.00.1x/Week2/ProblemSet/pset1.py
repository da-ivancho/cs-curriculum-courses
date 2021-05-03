def payDebtYear(balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: float -> the outstanding balance on the credit card
    annualInterestRate: float -> annual interest rate as a decimal
    monthlyPaymentRate: float -> minimum monthly payment rate as a decimal
    return float -> the remaining balance at the end of the year
    '''
    monthlyInterestRate = annualInterestRate / 12.0

    for month in range(1, 13):
        minMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    return round(balance, 2)

#Test Case
print('Remaining balance:', payDebtYear(42, 0.2, 0.04))
print('Remaining balance:', payDebtYear(484, 0.2, 0.04))
print('Remaining balance:', payDebtYear(368, 0.18, 0.06))