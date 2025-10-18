#WAP to define and call a fucntion that adds two numbers

def add(a,b):
    return (a+b)
print(add(5,7))


def add(a,b):
    print (a+b)
add(5,7)

#lambda
sum = lambda x,y: 7+8

#WAP with a fuction that takes a list as an argument and returns the sum of all its elements
list = [1, 2, 3, 4, 5]
def sum_of_list(list):
    sum = 0
    for i in list:
        sum = sum + i
        print(sum)
    return sum
print (sum_of_list(list))
print (sum_of_list([1,2,3,4,5]))