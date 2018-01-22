#Sam Krimmel
#1/22/18
#isItATriangle.py - tells whether three sides can make a triangle or not

a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))

l = max(a,b,c)
s = min(a,b,c)
m = ((a+b+c)-l)-s

print(l<s+m)
