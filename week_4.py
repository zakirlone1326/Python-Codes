#WAP to demonstrate the use of if, elif, else statements
'''
num = int(input("Enter a number : "))

if num >0:
    print("num is positive")
elif num <0 :
    print("num is negative")
else:
    print("you entered zero")

    '''

#WAP to print first n natural nums using for loop
'''
for i in range (1,11):
    print(i)
   '''

#WAP to print a pattern using nested loops 
#prints right angled triangle
'''
rows = int(input("Enter num of rows : "))
for i in range (1, rows + 1): # i represents curent row
    for j in range (rows - 1): #used to insert spaces
          print(" ", end=" ")
    for k in range(2 * i - 1): #used to insrt stars
        print("*", end=" ")
    print()
   '''

#prints acute triangle (pyramid)
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()