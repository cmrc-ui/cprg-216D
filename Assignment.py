#The Assignment
print("Welcome to the Grade Registry Program")
positive_answer = ['y','yes','yEs', 'YES', 'Yes']
negative_answer = ['no','n']
new = input("Would you like to add a new student?y(yes),n(n0): ").lower()
if new in positive_answer:
    while True:
        new_student = input("Enter the student's name:")
        print(new_student)
        print("Enter the student GPA for each subject. Enter -1 to stop entering GPA")
        GPA_count = 0
        total_GPAsum = 0
        GPA_input = float(input())
        while -1 <GPA_input <4.0:
            total_GPAsum += GPA_input
            GPA_count += 1
            GPA_input = float(input())
        if GPA_count > 0:
            print(total_GPAsum/GPA_count)
        elif GPA_input > 4:
            print("Invalid GPA")
        else:
            print("No GPA Input")
        new = input("Would you like to add a new student?y(yes)),n(n0): ")
        while new not in positive_answer and new not in negative_answer:
            print("Incorrect Input, please enter y(yes),n(no)")
            new = input("Would you like to add a new student?y(yes)),n(n0): ")
        if new in negative_answer:
            print("DONE")
            break
        
        
    



