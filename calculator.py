def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        return "cannot divide by zero"
    return  x / y

while True:

    print("select operation : ")
    print("1. add")
    print("2.  subtract")
    print("3. multiply")
    print("4. divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")
    if (choice =='5'):
        print("Acha chalta ho, thak gaye honnge sochte sochte, hahaha!")
        break
    
    num1= float(input("enter first numbe : "))
    num2= float(input("enter second number ; "))

    if (choice == '1'):
        print("Result of your operation is:" , add (num1, num2))
    elif (choice == '2'):
        print("Result of your operation is: ", subtract(num1, num2))
    elif (choice == '3'):
        print("Result of your operation is: ", multiply(num1, num2))
    elif (choice == '4'):
        print("Result of your operation is: ", divide(num1, num2))
    else:
        print("choose correct choice")