#list is collection of items
#operations on list
my_list = ["Zakir", 123, 45, 22.50]
print(my_list)
print(my_list*5) #prints elements 5 times
my_list.append("zeromiles") #append adds at last
my_list.remove(22.50) #removes 22.50
my_list.insert(1,"musadiq") #insert adds at  mentioned position
last=my_list.pop() #outputs last element
my_list.count("Zakir")
print(my_list)
#my_list.sort() #arranges them in ascending
print(my_list)
print(last)

'''movies = []
mov1=input("enter name of 1st movie: ")
mov2=input("enter name of 2nd movie: ")
mov3=input("enter name of 3 movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

movies.append(input("enter name of 1st movie")) #append adds items in list
movies.append(input("enter name of 2nd movie"))
movies.append(input("enter name of 3rd movie"))
print(movies)
'''

'''
print list but taking input from users
score =[]
for i in range(5):
    score1 = int(input(f"Enter {i+1} number:  "))
    score.append(score1)

print(score)'''
#print elements of following list
'''nums =[1, 4, 7, 10, 13, 15]
print (nums[0])
print (nums[1])
print (nums[2])
print (nums[3])
print (nums[4])
print (nums[5])'''

'''list1 = [1,2,3]
list2=[1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list2 == list2):
    print("palindrome")

else:
    print("not palandrome")'''

'''copy_list2= list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")

else:
    print("not palandrome")'''

