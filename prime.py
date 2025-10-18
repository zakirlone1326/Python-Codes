def is_prime():
    n=10
    for i in range(2,n):
        if(n<2):
            print("not prime")

        elif(n%i==0):
            print("not prime")
        else:
            print ("prime")