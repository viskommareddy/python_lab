"""
pyhton tuple-----------(1,3,8)
python list------------[1,3,8]

"""
# the major difference b/w tuple and list : tuple is immutable, i.e the values(items) in the tuple cant be changed
# where as the list is mutable , i.e the values (items) inside can be changed

my_tuple=(1,3,8)

print(my_tuple[0]) # it has the same indexation as list.

my_tuple[2]=12 # this gives an error , bcoz tuple is immutable. only the items in  a list are mutable

a=list(my_tuple) # converting a tuple into list. now it becomes mutable as it is converted to list.
