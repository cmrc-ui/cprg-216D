print("Average Checker!")
continue_option = 'y'
while continue_option == 'y':
        print("Please enter three numbers a,b,c")
        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))
        c = float(input("Enter 3rd number: "))
        average = float(a+b+c)/3
        print("The average is: ", average)
        continue_option = input("Would you like to input?y/n\t")