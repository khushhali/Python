# Compoound Intrerst Calculator

'''
For calculating compound intrest we need to have these data :-
1. Principle Amount
2. Rate of Intrest -> Yearly
3. Time Period -> For which amount is borrowed  -> In Years

Output of the program will be :-
1. Intrest Money
2. Toatl Amount -> Intrest + principle Amount

TA = p*(1 + r/100)**t - p
'''
print('#' + '-'*25 + '#'*15 + '-'*25 + '#')
print('|' + ' '*65 + '|')
print('|\t\t*Welcome To Compound Intrest Calculator*\t  |')
print('|' + ' '*65 + '|')
print('#' + '-'*25 + '#'*15 + '-'*25 + '#')
print()
print('Enter Below Asked Details For Calculating Compound Intrest')
# Taking Inputs From User
pAmt = float(input('1. Enter principle amount\t\t:- '))
roi = float(input('2. Enter rate of intrest (Yearly)\t:- '))
t = float(input('3. Enter time period (In Years)\t\t:- '))

# Calculating C.I.
tAmt = pAmt * (1 +  roi/100)**t

print()
print('Your Calculation Results Are Ready And Showen Below')
print(f'Intrest Amount\t:- {tAmt-pAmt : .2f}')
print(f'Total Amount\t:- {tAmt : .2f}')
print()
print('#' + '-'*25 + '#'*15 + '-'*25 + '#')
print('|' + ' '*65 + '|')
print('|\t\t*Thank You For Using Our Product*\t\t  |')
print('|' + ' '*65 + '|')
print('#' + '-'*25 + '#'*15 + '-'*25 + '#')
input('** Press Any Key To Exit')

