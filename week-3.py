#Task
username = input("Username:")
y = 3
if type(username) == str:
    print("Welcome,", username)
else:
    print("Invalid username")

#age calculator
year = input("Enter year of birth:")
year = int(year)
age = 2025 - year
print("Your age is:", age)