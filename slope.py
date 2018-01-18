#Sam Krimmel
#1/16/18
#slope.py - calculates the slope between two points

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('The slope is',(y2-y1)/(x2-x1))


print('y=mx+b')
if (x2-x1) == 0:
    print('Vertical line, not a function')
elif (y2-y1) == 0:
    print('Horizontal line at y =',y1)
else :
    m = ((y2-y1)/(x2-x1))
    print('m = ',m,'and b = ',(y1-(x1*m)))
