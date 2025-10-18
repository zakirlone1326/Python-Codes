#for loop is called entry loop
#while loop is called exit loop


#hello will print infity times
'''while True:
    print("hello")
'''

#hello will print 6 times
'''count =1
while count<=6:
    print("hello")
    count += 1'''
'''#will count upto 6
count =1
while count<=6:
    print(count)
    count += 1'''

#print numbers  from 1 to 100
'''a =1
while a<=100:
    print(a)
    a+=1'''

#print num from 100 to 1
'''a=100
while a>=1:
    print (a)
    a-=1'''

#print multiplication table of a num
'''a=3
b=1
while b<=10:
    print(a*b)
    b+=1'''
#user gives num
'''num= int(input("enter a number : "))
a=1
while a<=10:
    print (num*a)
    a+=1'''
#sum of first n natural nums
'''n= int(input("enter value for n : "))
sum = 0
i=1
while i <=n:
    sum +=i
    i+=1

print("total sum is: ",sum)'''

#factorial of first n nums 
'''n= int(input("enter a number : "))
fact = 1
i= 1
while i<=n:
    fact *=i
    i +=1

print ("factorial is : ", fact)'''

#print elements of following list using loop
'''nums = [1, 2, 3 , 4 ,5 ,6 ,7 ,8]
idx =0 #idx means index
while idx<len(nums):
    print(nums[idx]) #nums for printing elements. without nums idex are print
    idx +=1'''

    #search for a num x in this tuple using loop

'''nums =[1, 2, 7, 4, 5, 6, 7, 8] #nums is name of list
x= int(input("enter an element of list : ")) #element whose index we want to search

idx=0 
while idx<len(nums):
        if(nums[idx]==x):
                print("found at index ", idx)
        else:
                print("finding...")
      
        idx+=1'''

#continuos loop

'''i=0
while i<=5:
    
    if (i==3): #3 cant be print  
        i+=1
        continue
    print(i)
    i+=1'''


    #break loop
'''i=1
while i<=5:
    print(i)
    if (i==3): #gives nums only till 3
     break
    i+=1'''
#use of for loop to print elements 
'''nums =[1, 2, 3, 4, 5, 6, 7]
for val in nums:
    print(val)'''
#for loop for string
'''str = ["hello"]
for char in str:
    print(char)  '''

#note: else is used in for loop when using break in code

#print elements of list using loop
'''nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in nums: #el means elements we can write anything
    print(el)'''

#find element of tuple using for loop
'''
nums =(1, 4, 9, 16, 25, 36, 49, 64, 36, 100)
x = 36

idx = 0
for el in nums:
    if(el == x):
        print("number found at index", idx)
    idx +=1 '''
#range function

'''for i in range (1, 20, 2):#(start, stop , step) step means increment by
     print (i, end=" ") #prints all odd nums #end=" " prints on same line

print () #adds blank space

for i in range (2, 21, 2): 
    print (i, end=" ") #prints all even nums'''

#print nums from 1 to 100
'''for i in range (1, 101,1):
    print (i, end=" ")'''

#print nums from 100 to 1
'''for i in range (100, 0, -1):
    print(i, end=" ")'''

#print multiplication table of a number
'''num = int(input("enter a number ; "))
for i in range(1,11):
    print(num*i)'''

#pass statement
'''for i in range(5):
    pass #skips loop if we dont want to run loop
print ("hello")'''

#sum of first n natural nums
'''n= int(input("enter value for n : "))
sum = 0
for i in range(1, n+1): 
    sum +=i

print("total sum is: ",sum)'''

#factorial of first n nums 
'''n= int(input("enter a number : "))
fact =1
for i in range(1, n+1):
    fact = fact*i

print ("factorial = ", fact)'''

#print prime numbers
for i in range(2,40):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print(i)