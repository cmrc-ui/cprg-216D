#The Assignment
print("Welcome to the Grade Registry Program")
positive_answer = ['y','yes','yEs', 'YES', 'Yes']
negative_answer = ['no','n']
student_list = []
new = input("Would you like to add a new student?y(yes),n(n0): ").lower()
if new in positive_answer:
    while True:
        student_new = input("Enter the student's name:")
        print(student_new)
        print("Enter the student GPA for each subject. Enter -1 to stop entering GPA")
        GPA_count = 0
        total_GPAsum = 0
        GPA_input = float(input())
        if GPA_input == -1:
            break
        while GPA_input != -1:
            if GPA_input > 4:
                print("Invalid GPA")
            else:
                total_GPAsum += GPA_input
                GPA_count += 1
                GPA_input = float(input())     
        print(student_new,"'s GPA is: ",format(total_GPAsum/GPA_count,".2f"))
        student_list.append((student_new, round(total_GPAsum/GPA_count,2)))
        new = input("Would you like to add a new student?y(yes)),n(n0): ")
        while new not in positive_answer and new not in negative_answer:
            print("Incorrect Input, please enter y(yes),n(no)")
            new = input("Would you like to add a new student?y(yes)),n(n0): ")
        if new in negative_answer:
                print("GPA Calculator Ends - The list of Student's GPA are: (Student GPA)")
                break
for s in student_list:
     print(s[0],s[1])
