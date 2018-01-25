#Sam Krimmel
#1/22/18
#binary.py - asks user for 8 digit binary number and converts it into base 10

n = int(input('Enter an eight digit binary number: '))

fin = ((n//(10**7))*(2**7))+(((n%(10**7))//(10**6))*(64))+(((n%(10**6))//(10**5))*(32))+(((n%(10**4))//10000)*(16))+(((n%10000)//1000)*(8))+(((n%1000)//100)*(4))+(((n%100)//10)*(2))+((n%10))
print(fin)
