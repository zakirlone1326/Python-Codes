#input total rent, food ordered, electricity, charge per unit, persons in room
#total amout to pay

rent = int(input("Enter your flat rent  : "))
food =int (input("Enter the amount  of food : "))
electricity_points = int(input("Enter the electricity points for month : "))
charge_per_unit= int(input("Enter charge per unit : "))
Persons = int(input("Enter num  of persons living in room : "))

total = electricity_points*charge_per_unit
output = (food + rent + total)//Persons

print("Each person have to pay : ",output)


