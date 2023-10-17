"""
creaatinfg a new dictionary from a list
---syntax

new_dict={new_key:new_value for item in list}

creating a new dictionary from an existing dictionary
    --- syntax

new_dict = {new_key:new_value for (key,value) in dict.items()}

coditional dictionary comprehension
---syntax

new_dict = {new_key:new_value for (key,value) in dict.items() if test}  

"""

#example
student_names=["vishnu","srinivas","charan","praveen","nagendra","arjun"] #creating  a list
import random
# creating  a dictionary from a list
student_scores={student:random.randint(1,100) for student in student_names} 
print(student_scores)
#creating a dictionary from a dictionary and using condition
passed_students={student:score for (student,score) in student_scores.items() if score>=60 }
print(passed_students)

 
