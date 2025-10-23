#The Assignment
print("Welcome to the Grade Registry Program")
positive_answer = ['y','yes','yEs', 'YES', 'Yes']
negative_answer = ['no','n']
student_list = {}
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
            if GPA_input < 0 or GPA_input > 4:
                print("Invalid GPA, please input another number between 0 and 4") #use if input is other than -1
                GPA_input = float(input())
            else:
                total_GPAsum += GPA_input
                GPA_count += 1
                GPA_input = float(input())

        if GPA_count > 0:
           GPA_avg = format(total_GPAsum/GPA_count,".2f")
           print(f"{student_new}'s GPA: {GPA_avg}")
           student_list[student_new] =  GPA_avg

        new = input("Would you like to add a new student?y(yes)),n(n0): ")
        while new not in positive_answer and new not in negative_answer:
            print("Incorrect Input, please enter y(yes),n(no)")
            new = input("Would you like to add a new student?y(yes)),n(n0): ")
        if new in negative_answer:
                print("GPA Calculator Ends - The list of Student's GPA are: (Student: GPA)")
                break
for student, gpa in student_list.items():
     print(f"{student}: {gpa}")

"""
#dictionary - for assignment
gpas['Sam'] = 3.4 
print(gpas)
gpas['John'] = 4.8
 students_grades[name]=gpa
#note
students_grades = dict()



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
            if GPA_input < 0 or GPA_input > 4:
                print("Invalid GPA, please input another number between 0 and 4") #use if input is other than -1
                GPA_input = float(input())
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

"""


     
     

