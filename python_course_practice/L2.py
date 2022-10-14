#Part one

#The below strings will create my DOB

day = 20
year = 2000
month = "June"

#Concatenate each of these variables to create your full birthday.

my_birthday = month + " " + str(day) + ", " + str(year)

print(my_birthday)

#Part two

#Concatenate the variables first, second, third, and fourth and set this concatenation to the variable final:

first = "happy"
second = "birthday"
third = "to"
fourth = "you"

final = first + " " + second + " " + third + " " + fourth

#Print the final as uppercase

print(final.upper())

#Part three

age = 15

#Movie restrictions

Not_Permitted = age < 10
Permitted_with_parent = age < 15
Permitted_with_over18 = age < 18
Permitted_to_attend_alone = age >= 18

can_watch_movie = not Not_Permitted
print(can_watch_movie)

#Attendee can watch movie if not under 10. Must attend with parent