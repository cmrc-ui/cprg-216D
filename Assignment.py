#The Assignment
print("Welcome to the Grade Registry Program")
new = input("Would you like to add a new student?y(yes)),n(n0): ")
if new.lower() or new.upper() == 'yes':
    new_student = input("Enter the student's name:")
    print(new_student)
    total = 0
    print("Enter the student GPA for each subject. Enter -1 to stop entering GPA")
    sum = 0
    total = 0
    count = 0
    while total <= 4.0 and total > -1:
        sum += total
        total = float(input())
        count += 1
    count -= 1
    print(sum/count)
        
        
    



