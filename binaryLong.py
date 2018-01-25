#Sam Krimmel
#1/22/18
#binary.py - asks user for 8 digit binary number and converts it into base 10

n = int(input('Enter an eight digit binary number: '))

c1 = n//10000000
a = n%10000000
c2 = a//1000000
b = n%1000000
c3 = b//100000
c = n%100000
c4 = c//10000
d = n%10000
c5 = d//1000
e = n%1000
c6 = e//100
f = n%100
c7 = f//10
g = n%10
c8 = g

n1 = c1*(2**7)
n2 = c2*(2**6)
n3 = c3*(2**5)
n4 = c4*(2**4)
n5 = c5*(2**3)
n6 = c6*(2**2)
n7 = c7*(2**1)
n8 = c8*(2**0)

fin = n1+n2+n3+n4+n5+n6+n7+n8
print(fin)
