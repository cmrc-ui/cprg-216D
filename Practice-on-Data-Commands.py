"""
course = "CPRG"
greeting = "Welcome in"

list = ('adidas', 'puma', 'nike')

print(list)

print('first character is: ', greeting[0])

#Write a program that counts a number of alphabetic and digits character in a course name
result = 0
course_name = input('Course Name: ')
for character in course_name:
    result += 1
print('total characters are: ',result)

#or you can simply use len if you want
"""
"""
#LIST practice
playlist = ['Acoustics', 'Rock', 'Medley']
print(playlist)
print(playlist[1])
playlist.append('Drama')
print(playlist)
playlist[1] = 'Rock n Roll'
print(playlist)
"""
"""
#Noticed that in the output it includes [], so if you want to have no brackets, use the for loop

for choices in playlist:
    print(choices, end = "\t")
"""
"""
#For Tuple practice - similar to list but you cannot change your containers, once set.
playlist = ('1', 'Acoustics', '3Acoust')
print(playlist)
playlist[1] = 'Rock n Roll' # will output error unlike if LIST
"""
#For Dictionary - BEST OPTIOn, its keyed and flexible! Yung list mo changeable and mas easy, dito
#yung parang container mo is the 'Key', consider that keys should be unique
playlist = {'Acoustics':'Save You',"Rock N Roll":"Sweet Child of Mine", "Drama":"Cant Help"}
print(playlist["Acoustics"])
playlist["Acoustics"] = "Save You Again"
print(playlist["Acoustics"])

#For Sets - its like dictionary pero walang keys pero curl brackets dn ang representation. Kung ano
#key yun na rin yung value. To add, unlike dictionary na pag nagkaroon ka ng duplicate key, babaguhin
#niya ang data. Set will only print the unique data and its not in order. Ang use lang talaga niya
#is para makita mo ang unique data mo.
days = {'sun', 'mon', 'tues'}
