# #
# # class Person:
# #     def __int__(self, name, age, isMale, salary):
# #         self.salary = 0
# #     def display(self):
# #         print(f"Name: {self.name} \nAge: {self.age} \nMale? {self.isMale} \nSalary: R{self.salary:0f}")
# #
# #
# # name = input("Enter name: ")
# # age = input("Enter your age: ")
# # isMaleQ = input("Are you male? ")
# # if isMaleQ == "Y":
# #     isMale = True
# # else: isMale = False
# #
# # salary = 0
# #
# # firstPerson = Person(name, age, isMale, salary)
# # #firstPerson.display
#
# #region Lists
# #Lists: similar to arraylists
# # - Ordered, mutable (changable), but Mixed types you can have
# names = ['John', 'Mike', 'Ted', 21, 'Cwenga']
# names.append(45)
# names.insert(3, 999)
# names.remove('John')
# # print(names[2:4]) #Slicing
# # for n in names:
# #     print(n);
#
# #help(list)
# #print(len(names))
# #endregion
#
# #region Dictionaries
# #Dictionaries: similar to Map <K, V>
# #
# students = {
#     1:'Cwenga',
#     2:'Mike',
#     3:'Themba'
#     }
#
# students.get(5)
# students.values();
# students.pop(3);
# students.update({123 : 'Stevey'})
# print(students)
#
# students['234'] = 'Tank'
# print(students)
#
# #Iterating
# for student_no, student_name in students.items():
#     print(f"{student_no}: {student_name}")
# print("==========================================================================")
# print()
# print()
# print()
# print()
# #endregion
#
# #region Sets
# #Sets: Similar to HashSets
# #Unique, will remove duplicates, mutable
# student_numbers = {216377382, 2203345, 3243243}
# student_numbers.add(222293132)
#
# print("==========================================================================")
# print()
# print()
# print()
# print()
# #endregion
#
# #region Tuples
# #Tuples: Similar to final Array
# #No add or Remove
# #Fixed dataset
# names_tuple = ('Tim', 'Leo')
# names_tuple[0]
# names_tuple[2:4]
#
# print("==========================================================================")
# print()
# print()
# print()
# print()
# #endregion
#
# #region Logical Operators
# #and, or & not
# if True or not False:
#     print()
#
#
# #in, not in
# if "data" in "dataset":
#     print('true')
#
# if "Cwenga" not in names:
#     print("not in List")
# else: print("he's there")
#
# #is, is not
# #Checks if items have the same memory location / ID
# req_skills = ['Python', 'SQL', 'PowerBI']
# my_skills = ['Python', 'SQL', 'PowerBI', 'Java']
#
# if req_skills in my_skills:
#     print("has skills")
# else: print("not qualified")
#
# # &, |, ~ etc. BitWise Operators
# print()
# print()
# print()
# print()
# print("=============================================")
# print('Loops')
# print("=============================================")
# #endregion
#
# #region Loops
# student_list = ["dasda", "qdasdasd", "asdasdsa"] #Empty List
#
# # lookingFor = input("Enter student name: ")
# # for student in student_list:
# #     if lookingFor in student:
# #         print(lookingFor + " is in the list")
# #     else: print("Student not found")
#
#
# student_results = {
#     'Luke': 50,
#     'Tim':65,
#     'Albert':75,
#     'Cwenga': 61
# }
#
# print("Distinction students")
# for s in student_results:
#     print(s)
#
# for s_mark in student_results.values():
#     print(s_mark)
#
# #Cannot traverse a dictonary with index since its a MAP
# #BUT we can convert a dictionary to a list in order to be able to traverse it
#
# years_experience = {
#     'Mike':3,
#     'Kelly':6,
#     'Sim':12,
#     'James':3,
#     'Mary':4
# }
#
# years_experience_list = list(years_experience.items()) #Dictionary converted to List
# print(years_experience_list)
# print(years_experience_list[1])
#
# years = 0;
# i = 0;
# while i < 5: #We want the first 2 people with over 5 years experience
#     key, value = years_experience_list[i]
#     if value > 5:
#         print(years_experience_list[i])
#     i +=1
#
#
# print("First 2 individuals with more than 5 years of experience")
# i = 0;
# j =0;
# while i < 2:
#     key, value = years_experience_list[j]
#     if value > 5:
#         i += 1
#         print(years_experience_list[j])
#     j += 1
#
#
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
#
# #endregion
#
# #region List Comprehensions
#
# #endergion
#
# #region Practice
# data = [10, 20, 15, 30, 25]
#
# avg = 0;
# total = 0;
#
# above_avg = []
#
# for number in data:
#     total = total + number
#
# avg = total / len(data)
#
# for number in data:
#     if number > avg:
#         above_avg.append(number)
# #endergion

#Core Concepts Test
#Questions AI generated

#We want:
#region Challenge 1: fix the messy data returning a list of unempty unduplicated values

raw_inputs = ["  Data ", "Science", "", "data", "Analytics", "science", "  "]
raw_inputs_set = set()

for i in raw_inputs:
    i = i.strip().lower()
    if i != "":
        raw_inputs_set.add(i)

raw_inputs_set = sorted(raw_inputs_set)
print(raw_inputs_set)

#Output {'data', 'analytics', 'science'}
#endregion

#region Challenge 2: Extract ages > 21, Even & not equal to 42
ages = [18, 22, 25, 42, 60, 21, 44]

def extractAges(data):
    outputlist = []
    for i in data:
        if i > 21 and i%2 == 0 and i != 42:
            outputlist.append(i)
    print(outputlist)

extractAges(ages)

#Better way of writing this use LIST COMPREHENSIONS
outputlist = [i for i in ages if i > 21 and i %2 == 0 and i != 42]

#endregion

#help(list)