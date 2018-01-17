#Sam Krimmel
#1/17/18
#nameAge.py - asks name and age, prints how many letters in each name, and how old they will be in a year

name = input('Enter your first and last name: ')
age = int(input('Enter your age: '))

fname, lname = name.split()

print('Your first name has', len(fname), 'letters.')
print('Your last name has', len(lname), 'letters.')
print('Next year you will be', age+1, 'years old.')
