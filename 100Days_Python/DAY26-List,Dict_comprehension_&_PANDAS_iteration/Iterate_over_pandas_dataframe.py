# example for looping through dictionary

student_dict={
    "student":["vishnu","kiran","kartheek"],
    "score":[90,60,45]
              }
# looping throughn dictionary
for (student,score) in student_dict.items():
    print(student)
    print(score)
    
# creating a data frame from a dictionary
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# the process of looping through data frames is simplified using a iteration process
for (index,row) in student_data_frame.iterrows():
    if row.student=="vishnu":
        print(row.score)




