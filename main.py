#
# class Person:
#     def __int__(self, name, age, isMale, salary):
#         self.salary = 0
#     def display(self):
#         print(f"Name: {self.name} \nAge: {self.age} \nMale? {self.isMale} \nSalary: R{self.salary:0f}")
#
#
# name = input("Enter name: ")
# age = input("Enter your age: ")
# isMaleQ = input("Are you male? ")
# if isMaleQ == "Y":
#     isMale = True
# else: isMale = False
#
# salary = 0
#
# firstPerson = Person(name, age, isMale, salary)
# #firstPerson.display

#Lists: similar to arraylists
# - Ordered, mutable (changable), but Mixed types you can have
names = ['John', 'Mike', 'Ted', 21, 'Cwenga']
names.append(45)
names.insert(3, 999)
names.remove('John')
# print(names[2:4]) #Slicing
# for n in names:
#     print(n);

#help(list)
#print(len(names))

#Dictionaries: similar to Map <K, V>
#
students = {
    1:'Cwenga',
    2:'Mike',
    3:'Themba'
    }

students.get(5)
students.values();



#Sets

#Tuples