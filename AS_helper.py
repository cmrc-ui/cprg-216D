def show_menu():
    print("----Welcome to the student's record program----")
    print("What would you like to do today?")
    print("Find a student? Enter: 1")
    print("Edit a student's info using student ID? Enter: 2")
    print("Add a new student. Enter: 3")
    print("Remove a student. Enter: 4")
    print("Close the program. Enter 0")
    option = input("Input: ")
    return option

def add_student():
    positive_answer = ['y','yes','yEs', 'YES', 'Yes','YEs']
    negative_answer = ['no','n','N','NO','No','nO']
    student_list = {}
    while True:
        new = input("Would you like to add a new student? y(yes), n(no): ").lower()
        if new in positive_answer or new in negative_answer:
            break
        print("Incorrect input, please enter y(yes) or n(no).")
    if new in positive_answer:
        while True:
            student_new = input("Enter the student's name: ")
            print(student_new)
            print("Enter the student GPA for each subject. Enter -1 to stop entering GPA")
            GPA_count = 0
            total_GPAsum = 0
            GPA_input = float(input())
            #if GPA_input == -1:
            #break
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
            else:
                GPA_avg = 0
            print(f"{student_new}'s GPA: {GPA_avg}")
            student_list[student_new] =  GPA_avg

            new = input("Would you like to add a new student? y(yes), n(no): ").lower()
            while new not in positive_answer and new not in negative_answer:
                print("Incorrect Input, please enter y(yes), n(no)")
                new = input("Would you like to add a new student? y(yes), n(no): ").lower()
            if new in negative_answer:
                print("GPA Calculator Ends - The list of Student's GPA are: (Student: GPA)")
                break
    for student, gpa in student_list.items():
        print(f"{student}: {gpa}")
    return show_menu()
    


def remove_student():
    pass

def edit_studentname():
    pass

def search():
    pass

def run_search():
    pass

def run_edit():
    pass

def run_addstudent():
    pass

def run_remove():
    pass

def terminate():
    print("---Program Ends---")
    exit()
