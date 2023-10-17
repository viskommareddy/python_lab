#creating a list
state = ['alaska','arkansas','arizona','utah','washington','oregon','california']
#fetching the data using index
print(state[3]) #o/p is utah
#altering the data using index i.e list is mutable ,where as string is immutable.
state[3]='illinois'
print(state)
#adding a single item at the last position of the list using append()
state.append('Texas')
print(state)
#we can add a bunch of items i.e extenfd the list by using the extend()
state.extend(['kentuky','missori','alabama'])
print(state)
#we can concatinate two lists using +
s=state + ['massachusets','new hampshire','florida']
print(s)
#split function usage
names_string=input('enter all the names of the individuals followed by a comma')
name=names_string.split(',')
print(name)
print(name[0])


