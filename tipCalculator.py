#Sam Krimmel
#1/18/18
#tipCalculator.py - Calculates the amount to tip with given price of meal and percentage of tip

p = float(input('Price of Meal (in dollars): '))
t = int(input('Percent to tip: '))

print('You should tip $', round(((t*p)/100), 2))

