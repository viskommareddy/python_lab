#using for loop for range     ,converting the heights into int

student_heights=input('enter the heights of students followed by comma: ').split(',')
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

#for loop for calculating the sum of heights , instead of sum()

total_height=0
for height in student_heights:
    total_height+=height
print(f'the sum of all the heights={total_height}')

#for loop for counting the number of students, instead of len()

num_of_students=0
for student in student_heights:
    num_of_students+=1
print(f'the total number of students={num_of_students}')

#average height formula

avg_height=total_height/num_of_students
print(f'the avg height  of students ={avg_height}')