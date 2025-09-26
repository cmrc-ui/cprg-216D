"""
for i in range (1,51):

    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i% 3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")

    else:
        print(i)
"""
"""
#Eexercise 1 -Basic Math & Variable Assignment

year = int(input("Current Year:"))
age = input("Please enter your age: ")
age = year - int(age)
birthdate = year - age
print("I am ",birthdate, "years old")
print("The current year is ",year)
print("I was born in ", age)
"""
"""
#Exercise 2 - Simple Calculator
while True:
    num1 = (input("Enter first number: "))
    num2 = (input("Enter second number: "))
    if num1.lower() == "exit":
        print("invalid")
        break
    num1 = int(num1)
    num2 = int(num2)
    operation = input("Enter operation (+,-,*,/): ")
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("Invalid")
        else:
            print(num1/ num2)
    else:
        print("Invalid Operation")
"""
"""
#Exercise 3 Area Calculator
base = input("Any Number:")
height = input("Any Number:")
base = int(base)
height = int(height)
area = base * height
print("The area is:",area)
perimeter = 2 * base * height
print("The perimeter is:", perimeter)
"""
"""
#Exercise 4 Grade Calculator 
first_test = int(input("Grade of First Test:"))
second_test = int(input("Grade of Second Test:"))
third_test = int(input("Grade of Third Test:"))
average = (first_test * second_test * third_test)/3

if average >= 70:
    print("Congrats, you passed!")
else:
    print("Failed")
"""
"""
#Movie Ticket Pricing
customer_age = int(input("What is your age?:"))
if customer_age < 13:
        movie_price = 8
        print("Child","Price of the movie is: ",movie_price)
elif customer_age >= 13 and customer_age <= 18:
        movie_price = 12
        print("Student","Price of the movie is: ",movie_price)
elif customer_age >= 19 and customer_age <= 64:
        movie_price = 15
        print("Adult","Price of the movie is: ",movie_price)
else: 
        customer_age >= 65
        movie_price = 12
        print("Senior","Price of the movie is: ",movie_price)
movie_price = int(movie_price)
discount = movie_price - movie_price* 0.10
matinee_show = input("is this a matinee show? yes/no:")
if matinee_show == "yes":
    print("You qualify for matinee show!", "Ticket price would be: ", discount)
else:
    print("Ticket price would be:", movie_price)
        
"""
"""
#Odd Numbers Calculator

input1 = input("Ask for any positive number:")
input2 = input("Ask for any positive number:")
input1 = int(input1)
input2 = int(input2)
odd = []
for i in range (input1,input2+1):
    if i % 2 != 0:
        odd.append(i)

print("The odd numbers between",input1,"&",input2,"are:",(",".join(odd)))
"""
"""
#Printing all even numbers
even = []
for i in range(1,21):
    if i%2 == 0:
        even.append(str(i))
print("The even numbers are:",(" ,".join(even)),end = " ")
"""
"""
#Sum of First Natural N Number
natural = []
number = input("Input any number:")
number =int(number)
for i in range(1,number+1):
    natural.append(i)

print(f"The sum of all the numbers between 1 and {number+1}:",sum(natural))
"""

"""
#Finding the Largest of Three Numbers

while True:
    first = input("Input any number:")
    second = input("Input any number:")
    third = input("Input any number:")
    if first or second or third == "exit":
        print("invalid")
        break
first = int(first)
second = int(second)
third = int(third)
if second <= third:
    
else first <= second
not yet done
"""








