"""
list comprehension is a case of creating a new list from a previous list
---syntax
new_list=[new_item for item in list]

"""
# example

numbers=[1,2,3]

new_list=[n+1 for n in numbers]

print(new_list,len(new_list))

# list comprehension using strings

name="vishnu"

new_list1=[a for a in name]

print(new_list1,len(new_list1))

""" list range string tuple ---- these are called as sequences in python
"""
# list comprehension using sequences

range_list=range(1,5)# note,in range the upper limit is exclusive
new_range_lsit = [n*2 for n in range_list]
print(new_range_lsit)

""" conditional list comprehension
--- syntax
new_list=[ new_item for item in list if test]
"""
names=['vishnu','srinivas','redd','manojkumar','praveen']
short_names=[n.upper() for n in names if len(n)<5]
long_names=[n.upper() for n in names if len(n)>5]
print(short_names)
print(long_names)

 