'''def add(a,b):
    return (a+b)
sum = add(4,5)
print(sum)

def student(name):
    return f"Hello , {name}"
print(student("zakir"))

#area of square
import math as m
area= m.pi*m.pow(5,2) #pow-->power contains base and exponent
print(area)'''

#functions with inputs
def greet(name):
    return f"hello! {name}"
print(greet("zakir"))

def add(a,b):
    return (a+b)

print(add(60,80))

def area(a,b):
    return a*b
print("Area of rectangle: ",(area(4,6)))

def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()
greet("Zakir")

def print_item(items):
    for item in items:
        print("-", item)
colors=["red", "green", "blue"]
print_item(colors)