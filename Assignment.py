#The Assignment
print("Welcome to the Grade Registry Program")
new = input("Would you like to add a new student?y(yes)),n(n0): ")
if new.lower() or new.upper() == 'yes':
    new_student = input("Enter the student's name:")
    print(new_student)
    print("Enter the student GPA for each subject. Enter -1 to stop entering GPA")
    GPA_count = 0
    total_GPAsum = 0
    GPA_input = float(input())
    while GPA_input <= 4.0 and GPA_input > -1:
        total_GPAsum += GPA_input
        GPA_count += 1
        GPA_input = float(input())
    GPA_count -=1
    print(total_GPAsum/GPA_count)
        
        
    



