#swap using 3rd virable
a=5
b=6
print ("Orginal values : ", a,b)
c=a
a=b
b=c
print ("Swapped values : ", a,b)

#swap without using 3rd virable
a=10
b=20
print("Orginal values : ", a,b)
a,b=b,a
print("Swapped values : ", a,b)

#taking values from user

num1= int(input("Enter first num : "))
num2= int (input("Enter second number : "))

print("Values before swapped : ", num1,num2)
num1, num2 = num2, num1
print("Values after swap : ", num1, num2)