# Menu of resto
menu ={
    'pizza':  400,
    'pasta':  300,
    'coffe':  100,
    'shake':  140,
    'steak':  250
}

print() #inserts a blank line bw two lines
print("Hello, Welcome to Zeromiles Kupwara")

print() 

print("\n pizza: ₹400\n pasta: ₹300\n coffe: ₹100\n shake: ₹140\n steak: ₹250")

order = 0 #we have zero order at starting
print() 
item_1= input("Enter the name of item you want to order : ")
if item_1 in menu:
    order += menu[item_1] #increment in num of order
    print("Yay!, Item has been added successfully!")
else:
    print("Sorry, your item", item_1, "is not availible!")

another_order = input("Do you want to add items? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")

    if item_2 in menu:
        order += menu[item_2] 
        print("Yay!, Item", item_2, "has been added to order!")
    else:
        print("Sorry, Ordered item", item_2, "is not availible!")
        
final_choice = input("Do you want the bill or add more ? : ")
if final_choice == "bill":
    print("Thank you, Your bill is rupee : ₹", order, "only")
else:
    print("Sorry, You can order only two orders at a time")

print()


