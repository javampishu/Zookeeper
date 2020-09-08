# put your python code here

# input number of students in each group
stud_first_group = int(input())
stud_second_group = int(input())
stud_third_group = int(input())

# calculate the total amount of students

desk = ((stud_first_group + 1) // 2)
desk = desk + (stud_second_group + 1) // 2
desk = desk + (stud_third_group + 1) // 2

# printing desks count
print(desk)
