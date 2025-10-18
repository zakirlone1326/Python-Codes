#WAP to create a list, perform slicing and append elements to it
'''
my_list= ["kupwara", "baramulla","bandipora"]
print(my_list) #prints elements of list

print(my_list[1:3]) #will print elements at index 1 and 2 because it excludes  upper limit

#now append elements in my_list
my_list.append("Sopore") #this will add sopore in my list at the end
print(my_list) #output will be all elements of list after append
'''

#WAP to demonistrate use of tuple data type and its operations

my_tuple= (3,2,3,4,5)

print(my_tuple)
print(len(my_tuple))  #prints length of tuple
print(my_tuple[2]) #prints element at index 2
print(my_tuple.index(5))  #prints the index value of element 5
print(my_tuple.count(3)) #pritns frequency of 3
print(my_tuple[1:4]) #prints 1st,2nd,3rd element
print(my_tuple*2) #prints tuple 2 times

#WAP to find length, maximum, minimum value of list

my_list=[3,5,7,9,1]
print(my_list)
print(len(my_list)) #prints length of list
print(max(my_list))  #prints maximum value present in list
print(min(my_list)) #prints minimum value present in list