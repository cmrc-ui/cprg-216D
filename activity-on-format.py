x = 12345.6789
y = 12345.6789
z = 12345.6789
a = 0.5
b = 123
c = -123
d = "Hello"
x1 = 200
x2 = 1000
x3 = 30000
print(format(x,",.2f"))
print(format(y, "14,.2f"))
print(format(z,".2e"))
print(format(a,"%"))
print(format(b,"d"))
print(format(c,"7d"))
print(format(d, "10s"))
print("Your value is {1:.3f} years old, another value is {0:.2e}, last value is {2:.0%}".format(x1,x2,x3))
    #usually wala yung {} if by default hindi mo nilagyan ng number ibabase nya ng order based sa
    #format() mo, if may number then iffollow niya yung order ng number

    #regarding {1:.3f} if gusto mo may three decimal places ung 2nd input which is x2 then ganito gawin m
    #OR YOU CAN ALSO DO BELOW PRINT FORMAT
print(f"x is {x1:.3f} and y is {x2:.2e}")

name1 = 'John'
name2 = 'Sarah'
print(f'name is: {name1:>20}') #extra 20 characters to the left
print(f'name is: {name2:^20}') #extra characters is at the middle

#Program to make CAD Table
yesterday_value = 0.7588
today_value = 0.7479
change_value = today_value - yesterday_value
print("{:>10s}{:>10s}".format("Date", "Rate")) #kaya 10 yung gusto mong extra characters kasi para macover ang pagshift sa "yesterday" which has 9 charaters
print("{:>10s}{:>10s}".format("===", "==="))
print("{:>10s}{:>10.4f}".format("Yesterday", yesterday_value))
print("{:>10s}{:>10.4f}".format("Today", today_value))
print("{:>10s}{:>10.4f}".format("Change", change_value))

print(f'Date')
