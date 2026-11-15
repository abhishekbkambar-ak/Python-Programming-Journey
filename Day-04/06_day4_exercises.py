# Day 4 Exercises 

# 1st Exercise      [ info of student ]
print("\n------ MY PROFILE ------")
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")
college = input("Enter college name : ")

print(f"My name is {name}")
print(f"My age is {age}")
print(f"I live in {city}")
print(f"I am Studing at {college}")

# 2nd Exercise       [ Addition ]
print("\n------ Addition ------")
a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))

print(f"The sum of this two number is {a+b}")

# 3rd Exercise      [ Age Calculator ]
print("\n------ Age calculator ------")
birth_year = int(input("Enter your Birth year : "))
current_year = 2026

print(f"Your current age is : {current_year - birth_year}")

# 4th Exercise          [ Rectangle Calculator ]
print("\n------ Rectangle calculator ------")
length = float(input("Enter a length : "))
width = float(input("Enter a width : "))

area = length * width
perimeter = 2 * (length + width)

print(f"The area is : {area: .2f}")
print(f"The perimeter is : {perimeter: .2f}")

# 5th Exercise  [ Percentage Calculator ]
print("\n------ Marks percentage ------")
Kannada = int(input("Enter your kannada marks : "))
English = int(input("Enter your english marks : "))
Hindi = int(input("Enter your hindi marks : "))
Math = int(input("Enter your math marks : "))
science = int(input("Enter your science marks : "))
social_science = int(input("Enter your social science marks : "))

Subjects = Kannada + English + Hindi + Math + science + social_science

print(f"Your all subject percentage is {(Subjects/600)*100}% ")
