#three forms of if statement

"""
1) if statement

is_adult = True

if is_adult:
    print("Yes, Its adult") #if its false it will be ignored

2) if else statement

age = 17
if age>=18:
    print("you can drive")
else
    print("you cannot drive")

3) if elif else statement (many conditions)

work = False
gym = True
go_out = False
home = True

if work: 
    print("I will me sam")
    print("We will have lunch together")
if gym:
    print("I will go to gym")
elif go_out:
    print("I will go out")
elif home:
    print("I will stay at home")
else:
    print("I will sleep")   
    """

#Nested If
"""
print("Welcome to the party")
user_input = input("Please enter your age")
age = int(user_input)
gender = input("Please enter your gender: M or F")
if age >= 18:
    if gender == "M":
        print("You can go to the men's party")
    else:
        print(" You can go to women's party")
else:
    print("You cannot enter the party") 

"""

#match statement (better to have if you have specific condition not using greater than or less than)

subject = input("Please enter your subject: Math, Science, English")
match subject:
    case "Math":
        print("You have Math at 9am")
    case "Science":
        print("You have Science at 10am")
    case "English":
        print("You have English at 11am")
    case _:
        print("Invalid Subject")