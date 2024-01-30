
#If a,b,c are three sides of a triangle
print('To find the area of a triangle')

a=float(input('Enter first side:'))
b=float(input('Enter second side:'))
c=float(input('Enter third side:'))

#calculate the semi-perimeter
s=(a+b+c)/2

#calculate teh area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is %0.2f'%area)


#In this program, area of the triangle is calculated
#when three sides are given using Heron's formula.
