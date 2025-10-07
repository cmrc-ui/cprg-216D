"""
while statemnt

if condition:  #runs only once if the condition is true
    statement1
    statement2

while condition: #the statement run as long as the condition is true
    statement1
    statement2

"""

"""Sum of 1 to 100
sum = 0
counter = 1 
while counter <= 100:
    sum+= counter
    counter += 1
print("sum of first 100 natural numbers is:", sum)
"""

"""
Factorial of a number
factorial = 1
counter = 1
while counter <=10:
    factorial *= counter
    counter += 1
print("Factorial of 10 is:", factorial)
"""

""" 
#1 to 10 Counter
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
"""
"""
#Print even numbers from 2 to 20
counter = 2
while counter <= 20:
    if counter %2 == 0:
        print(counter)
    counter += 2
"""
"""
#Even COunter
counter = 0
while True:
    number = input("Enter a number(or exit to quit):")
    if number.lower() == "exit":
        print("program ends")
        break
    number = int(number)
    if number %2 == 0:
        counter += 1
    else:
        pass
print("total number of even:",counter)
"""
"""
#Printing the largest number
number1 = int(input("First Number: "))
number2 = int(input("Second Number: "))
number3 = int(input("Third Number: "))

highest = number1

if(number2 > highest):
    highest = number2
    if(number3 > highest):
        highest = number3
print(highest)
"""
"""
#if passer
grade = input("Input the Grade: ")
grade = float(grade)
if grade >= 90 and grade <= 100:
    print("A")
elif grade <= 89 and grade >= 80:
    print("B")
elif grade <= 60:
    print("Failed")
"""
"""
number = input("Any number:")
number = int(number)
counter = 1
while counter <= number:
    counter += 1
    print(counter-1)
    
"""
"""
#The Assignment
total = 0
while True: 
    GPA = input("Enter the student GPA. Enter -1 to stop entering GPA")
    student = input("Enter a)
    if GPA.lower() == "-1":
        print("Program ends")
        break
    GPA = float(GPA)
    if total 
"""
print("Average Checker!")
while True:
    instruction = input("Would you like to check average?(y/n)")
    if instruction.lower() == 'n':
        print("Program ends")
        break
        
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    c = float(input("Enter 3rd number: "))
    if instruction == 'y':
        average = float(a+b+c)/3
        print("The average is: ", average)
    
        
    
    