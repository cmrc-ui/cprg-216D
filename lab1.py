"""
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
"""
#Average chekcker but have infinite inputs with range greater than -20 as sign to stop
print("Average Checker!")
continue_option = 'y'
while continue_option == 'y':
        print("Please enter the numbers, one at a time.")
        sum = 0
        num = 0
        count = 0
        while num>-10 and num <20:
                sum += num
                num = float(input())
                count += 1
        count -= 1
        print(sum/count)
        continue_option = input("Would you like to input?y/n\t")
