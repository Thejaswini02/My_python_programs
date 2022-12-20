def triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

a=float(input("enter length of side a:"))
b=float(input("enter length of side b:"))
c=float(input("enter length of side c:"))
if triangle(a,b,c):
    print('triangle is valid')
    s=(a+b+c) / 2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print('triangle area=',area)
else:
    print('triangle is invalid')
