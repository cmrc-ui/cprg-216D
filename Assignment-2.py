import AS_helper
from AS_helper import show_menu, add_student, terminate


while True:
    choice = show_menu()

    if choice == '3':
        add_student()
    elif choice == '0':
        terminate()
    else:
        if choice not in ['1','2','3','4']:
            print("Input Invalid")
            break
    break



