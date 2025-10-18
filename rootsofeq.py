#finding roots of quadratic equation
'''import math #math is used to find only real roots
a=1
b=-7
c=10
d= b**2-4*a*c

root1= (-b+math.sqrt(d))/(2*a)
root2= (-b-math.sqrt(d))/ (2*a)

print("root 1 : ", root1)
print("root 2 : ", root2)'''



#finding roots of quadratic equation

import cmath #cmath is used to find both real and imaginary roots

a=1
b=6
c=10
d=b**2-4*a*c

root1=(-b+cmath.sqrt(d))/(2*a)
root2=(-b-cmath.sqrt(d))/(2*a)

print("root 1 is : ", root1)
print("root 2 is : ", root2)