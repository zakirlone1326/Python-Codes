#function is block of statements that perform specific task
#def is keyword for function
#func help to wite clean, efficient and reusable code


#sum of two nums using func
'''def add(a,b):
    sum = a+b
    return a+b

sum = add(1,2) #1 and 2 are arguments
print (sum)

sum = add(4,5)
print(sum)

sum= add(10,20)
print(sum)'''

#note: we did not write seperate functs for multiple adds but only one

#print string using func

'''def name(): #parameterless func
    print("zakir")

name()
name()
name()
#zakir will be print 3 times'''

#function prints none due to unavailiblity of return type
'''def name():
    print("zakir")
print (name()) #this will print none because funct is in ()
'''

#avg of 3 nums using func
'''a=10
b=11
c=12
def avg( a,b,c):
    print((a+b+c)/3)
    # return (a, b, c)
avg(a,b,c)'''

#avg of 3 nums using func

'''def avg(a,b,c):
    sum=a+b+c
    avg=sum/3 # 3 is number of arguments in func
    print(avg)
    return(avg)

avg(1,2,3)
avg(4,5,6)
avg(12,11,10)'''

#product of two nums
'''def multiply(a, b): #can put values of a and b here LAO IF WE DONT wwant to mention at calling time
    print(a*b)
    return(a,b)
multiply(2,6)''' #we can also declare value of first argument when declaring func but not for 2nd

#length of list
'''cities =["kupwara", "sopore", "baramulla"]
def length (list): #list is an argument here
    print(len(list))
    
length(cities)
print (cities[0]) #output kupwara'''

#fact  using func

'''def fact  (n):
    fact=1
    for i in range(1, n+1):
     fact = fact*i
    print(fact)

fact (5) #will find 5 fact '''

#convert usd $ into INR rupee
'''def converter (usd_val): 
    inr_val = usd_val * 83 #83 means 1 $=83 rupees
    print(usd_val, "USD =", inr_val, "INR")

converter (10) #converts 10$ into INR'''

#func to print even odd
'''num= (int(input("enter a num : ")))
def even_odd(num): #a means func will take one argument
    if (num%2==0):
        print("even")
    else:
        print("odd")
even_odd(num) #func call'''


#func to print even odd using encapsulation
'''def Even_odd ():
    num = int(input("Enter a num : "))
    if (num%2==0):
        return"Even"

    else:
        return"Odd"
Even_odd()
    '''

#fibonacci series
'''n= int(input("Enter a num : "))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y'''

