
class Person:
    def __int__(self, name, age, isMale, salary):
        self.salary = 0
    def display(self):
        print(f"Name: {self.name} \nAge: {self.age} \nMale? {self.isMale} \nSalary: R{self.salary:0f}")


name = input("Enter name: ")
age = input("Enter your age: ")
isMaleQ = input("Are you male? ")
if isMaleQ == "Y":
    isMale = True
else: isMale = False

salary = 0

firstPerson = Person(name, age, isMale, salary)
firstPerson.display
