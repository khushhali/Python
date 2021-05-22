'''
simple int calculator
'''
'''
principe amt, rate, time, intrest, total amount
'''

print('enter below details:-')
pAmt = float(input('enter your principal amount:-'))
r = float(input('enter your rate of interest(yearly):-'))
t = float(input(' enter time period (in years):-'))

intr = (pAmt*r*t)/100
print('your total intrest is=',intr)
tAmt = intr + pAmt
print('your tottal amount is=',tAmt)


# Compound intrest


