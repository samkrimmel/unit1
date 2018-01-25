#Sam Krimmel
#1/22/18
#isItATriangle.py - tells whether three sides can make a triangle or not

a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))

print((max(a,b,c))<(min(a,b,c))+(((a+b+c)-1)-(min(a,b,c))))
