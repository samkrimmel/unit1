#Sam Krimmel
#1/22/18
#change.py - takes in amount of money and prints how many quarters, dimes, nickels, and pennies you need to make up that amount

cash = int(input('Amount of money in cents: '))

quar = cash//25
dime = (cash - 25*quar)//10
nick = (cash - (dime*10 + quar*25))//5
penn = cash - (dime*10 + quar*25 + nick*5)

print('Quarters: ', quar)
print('Dimes: ', dime)
print('Nickels: ', nick)
print('Pennies: ', penn)
