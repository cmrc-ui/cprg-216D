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