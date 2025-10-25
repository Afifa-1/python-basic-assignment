Student = [("Ali", 85), ("Ahmed", 85), ("Ali", 85), ("Zara", 92), ("Sara", 90)]

print("list:", Student)

Student = list(set(Student))
print("After removing duplicates:", Student)

total_marks = 0
count = 0

for student in Student:
    total_marks = total_marks + student[1]  
    count = count + 1

average_marks = total_marks / count
print("\nAverage marks:", average_marks)

names_list = []
for student in Student:
    names_list.append(student[0])  

print("List of names only:", names_list)

names_tuple = tuple(names_list)
print("Tuple of names:", names_tuple)

student_to_find = "Sara"
if student_to_find in names_tuple:
    print(f"\n{student_to_find} is in the tuple!")
else:
    print(f"\n{student_to_find} is not in the tuple!")
