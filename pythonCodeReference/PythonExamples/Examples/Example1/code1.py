color = ["red", "blue", "green"] 
print(color) 
  
color[0] = "pink"
color[-1] = "orange"
print(color) 

# import functools

# user = {"username": "jose", "access_level": "user"}


# def make_secure(access_level):
#     def decorator(func):
#         @functools.wraps(func)
#         def secure_function(*args, **kwargs):
#             if user["access_level"] == access_level:
#                 return func(*args, **kwargs)
#             else:
#                 return f"No {access_level} permissions for {user['username']}."

#         return secure_function

#     return decorator


# @make_secure("admin")  # This runs the make_secure function, which returns decorator. Essentially the same to doing `@decorator`, which is what we had before.
# def get_admin_password():
#     return "admin: 1234"


# @make_secure("user")
# def get_dashboard_password():
#     return "user: user_password"


# print(get_admin_password())
# print(get_dashboard_password())

# user = {"username": "anna", "access_level": "admin"}

# print(get_admin_password())
# print(get_dashboard_password())

# import functools


# user = {"username": "jose", "access_level": "guest"}


# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function(panel):
#         if user["access_level"] == "admin":
#             return func(panel)
#         else:
#             return f"No admin permissions for {user['username']}."

#     return secure_function


# @make_secure
# def get_password(panel):
#     if panel == "admin":
#         return "1234"
#     elif panel == "billing":
#         return "super_secure_password"


# print(get_password.__name__)

# import functools


# user = {"username": "jose", "access_level": "guest"}

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."

#     return secure_function


# @make_secure
# def get_admin_password():
#     return "1234"


# print(get_admin_password.__name__)



# user = {"username": "jose", "access_level": "guest"}


# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."

#     return secure_function


# @make_secure
# def get_admin_password():
#     return "1234"

# print(get_admin_password())





# def make_secure(func):
#     def secure_function():
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for {user['username']}."

#     return secure_function


# get_admin_password = make_secure(get_admin_password )  # `get_admin_password` is now `secure_func` from above

# user = {"username": "jose", "access_level": "guest"}
# print(get_admin_password())  # Now we check access level

# user = {"username": "bob", "access_level": "admin"}
# print(get_admin_password())

# def bool_return():
#     try:
#         return True
#     finally:
#         return False

# bool_return()

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except (RuntimeError, TypeError, NameError,ValueError):
#          print("Oops!  That was no valid number.  Try again... ")
    


# import math 
# print(math.pi) 

# from typing import List  # , Tuple, Set, etc...


# class Book:
#     pass

# class BookShelf:
#     def __init__(self, books: List[Book]):
#         self.books = books

#     def __str__(self) -> str:
#         return f"BookShelf with {len(self.books)} books."

# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
 
#     def get_total(self):
#         return (self.pay*12)
 
 
# class Employee:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.obj_salary = Salary(self.pay)
 
#     def annual_salary(self):
#         return "Total: " + str(self.obj_salary.get_total() + self.bonus)
 
 
# obj_emp = Employee(600, 500)
# print(obj_emp.annual_salary())


# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"

#     def disconnect(self):
#         self.connected = False



# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         # super(Printer, self).__init__(name, connected_by)  - Python2.7
#         super().__init__(name, connected_by)  # Python3+
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

#     def print(self, pages):
#         if not self.connected:
#             raise TypeError("Device is disconnected at this time, cannot print.")
#         print(f"Printing {pages} pages.")
#         self.remaining_pages -= pages


# printer = Printer("Printer", "USB", 500)
# printer.print(20)
# print(printer)
# printer.print(50)
# print(printer)
# printer.disconnect()
# printer.print(30)



# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#     @staticmethod
#     def static_method():
#         print(f"Called static_method. We don't get any object or class info here.")

# instance = ClassTest()
# instance.instance_method()
# ClassTest.class_method()
# ClassTest.static_method()


# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")

# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

     

# class DateTime(object):

#     def __init__(self, day=10, month=10, year=2000):
#         self.day = day
#         self.month = month
#         self.year = year

#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split('-'))
#         myDate = cls(day, month, year)
#         return myDate

#     @staticmethod
#     def is_valid_date(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999

# dateObj = DateTime.from_string('20-05-1994')
# is_valid_date = DateTime.is_valid_date('20-05-1994')
# print(is_valid_date)


# class Student(object):

#     @staticmethod
#     def is_full_name(name_str):
#         names = name_str.split(' ')
#         return len(names) > 1

# Student.is_full_name('Scott Robinson')   # True
# Student.is_full_name('Scott')            # False

# print (Student.is_full_name('Scott Robinson'))    
# print (Student.is_full_name('Scott'))  


# class Vector3(object):
#     def __init__(self, args):
#         self.x = args[0]
#         self.y = args[1]
#         self.z = args[2]

#     def __str__(self):
#         return "x: {0}, y: {1}, z: {2}".format(self.x, self.y, self.z)

#     def __repr__(self):
#         return "Vector3([{0},{1},{2}])".format(self.x, self.y, self.z)

# v = Vector3([1,2,3])
# print (str(v))     #x: 1, y: 2, z: 3
# print (repr(v))    #Vector3([1,2,3])        

# class Person:
#     name = ""
#     age = 0

#     def __init__(self, personName, personAge):
#         self.name = personName
#         self.age = personAge

#     def __repr__(self):
#         return {'name':self.name, 'age':self.age}

#     def __str__(self):
#         return 'Person(name='+self.name+', age='+str(self.age)+ ')'

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         # I'm adding the < > just so it's clear that this is an object we're printing out!
#         return (
#             f"<Person({self.name!r}, {self.age})>"
#         )  # !r calls the __repr__ method of the thing.


# bob = Person("Bob", 35)
# print(bob)

# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (89, 90, 93, 78, 90)

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student()
# print(student.name)
# print(student.average())

# class Student:
#     def __init__(self, name, *grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student("Bob", 36, 67, 90, 100, 100)
# print(student.average())

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student("Bob", (36, 67, 90, 100, 100))
# print(student.average())

# class Student:
#   def __init__(type, name):
#     type.name = name

#   def namefunc(abc):
#     print("student name is " + abc.name)

# student = Student("Rolf")
# student.namefunc()

# class Student:
#     def __init__(self):
#         self.name = "Rolf"
#         self.grades = (89, 90, 93, 78, 90)

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student = Student()
# print(student.average())

# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234"),
# ]

# username_mapping = {user[1]: user for user in users}
# userid_mapping = {user[0]: user for user in users}

# print(username_mapping)

# print(username_mapping["Bob"])  # (0, "Bob", "password")

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")


# # Initialize the `fahrenheit` dictionary 
# fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# # Get the corresponding `celsius` values and create the new dictionary
# celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

# print(celsius)
# # Initialize `fahrenheit` dictionary 
# fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

# #Get the corresponding `celsius` values
# celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

# #Create the `celsius` dictionary
# celsius_dict = dict(zip(fahrenheit.keys(), celsius))

# print(celsius_dict)

# # Use dictionary comprehension
# numbers = range(10)
# new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

# print(new_dict_comp)


# numbers = range(10)
# new_dict_for = {}

# # Add values to `new_dict` using for loop
# for n in numbers:
#     if n%2==0:
#         new_dict_for[n] = n**2

# print(new_dict_for)

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# dict1_keys = {k*2:v for (k,v) in dict1.items()}
# print(dict1_keys)

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Double each value in the dictionary

# double_dict1 = {k:v*2 for (k,v) in dict1.items()}
# print(double_dict1)


# user_age = input("Enter Your age: ")
# years = int(user_age)
# months = years * 12
# print(f"Your age, {years}, is equal to {months} months.")


# friends = ["Rolf","Bob","Jen"]
# for friend in friends:
#   if friend == "Bob":
#     continue
#   print(f"{friend} is my friend")

# numbers = [1, 2, 3, 4]
# squares = [n**2 for n in numbers]

# print(squares)

# friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

# print(friend_ages["Adam"])

# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# x, y = (5, 11)

# print(x)
# print(y)

# person = ("Bob", 42, "Mechanic")
# name, _, profession = person

# print(name, profession)  # Bob Mechanic

# def say_hello(name,surname):
#     print(f"Hello, {name}  {surname}")


# say_hello("Smith",surname="Bob") 
