# Simple and Compound Interest

# Reading principal amount, rate and time
principal = float(input('Enter amount: ₹ '))
time = float(input('Enter time: '))
rate = float(input('Enter rate: '))

# Calcualtion0
simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)**time - 1)
# Calculating interest rate per month
r = rate/(12*100)
time = time*12
#the final amount per total year 
total_amount = (simple_interest+principal)

# Calculating Equated Monthly Installment (EMI)
emi = principal * r * ((1+r)**time)/((1+r)**time - 1)

# Displaying result
print("Monthly EMI = ₹", emi)
print('Simple interest is: ₹ %f' % (simple_interest))
print('Compound interest is:₹ %f' %(compound_interest))
print('the total amount in %d years is ₹ %f' %(time,total_amount))
