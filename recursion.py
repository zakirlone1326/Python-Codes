#concept where a func calls itself repeatedly

#number till 0
'''def show(a): #show is func name w
    if a==0: #when a reaches 0 func will return which means code will stop. it can be negative as well
        return #in case we dont use if and retun case it will execute infinitely
    print(a)
    show(a-1) #used to show nums less than input num means decrement in 'a' by 1
show(10) '''#10 means nums from 10 to 1 

#factorial
'''def  fact(n):
    if (n==0 or n==1):
        return  1
    else:
        return n* fact(n-1)
    
print(fact(5))'''

#it works in a sense where the num whose fact we are searching asks for its previous nums fact repeatedly

#sum of first n natural nums
'''def cal_sum(a):
    if(a==0):
        return 0
    return cal_sum(a-1) + a
result = cal_sum(10) #sum of nums is stored in result variable
print(result)'''

'''#print elements in a list
def print_list(list, idx):
    if(idx == len(list)):
     return
     print(list[idx]) 
    print_list(list, idx+1)
            
fruits =["Mango", "litchi", "cherry"]
print(fruits)'''

#sum of digits

'''def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
    
print(sum_of_digits(1234))'''

#power of a num
'''def power_of_num(m,n): 
    if(n==0):
      return 1
    elif (m==1):
       return 1
    else:
       return m* power_of_num(m,n-1)
    
print(power_of_num(1,10))'''

#fibonacci series using func
def fibo(n):
    if(n==0):
     return 0
    elif(n==1):
       return 1
    else:
       return fibo(n-1)+fibo(n-2)

print(fibo(6))