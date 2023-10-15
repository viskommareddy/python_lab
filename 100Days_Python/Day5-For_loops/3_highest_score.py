# using for loop for range

student_scores=input('enter the scores of the students followed by a space: ').split('')
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])

# using for loop to get the highest score , instead of max()

highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f'the hightest score is {highest_score}')