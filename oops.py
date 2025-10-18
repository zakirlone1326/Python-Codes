#class is a blueprint

#creating class of objects
'''class Students:
     name="zakir"

 s1 = Students()
 print(s1) #prints address
 print(s1.name)'''

#FACTORY
'''class Car:
    color= "blue"
    brand = "hyundai"
car1= Car()
print(car1.color)

car2= Car()
print(car2.color)
print(car2.brand)'''

#calling diff arguments
'''campus_name="North campus" #since this is same for all we declare it here
class Students:
    def __init__(self, name, marks, course): #parameterised constructers, if we have only self argument then it is called default constructor
        self.name=name #self.argument helps to store different names
        self.marks=marks
        self.course=course
        print("adding members : ")

s1= Students("Zakir", "80","MCA")
print(s1.name, s1.marks, s1.course)

s2=Students("Mariya","98","MCA")
print(s2.name,s2.marks,s2.course)'''

#if class and object attribute is same, prioirty is given to objects
