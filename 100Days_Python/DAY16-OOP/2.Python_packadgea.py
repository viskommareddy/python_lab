from prettytable import  PrettyTable    
# pretty table is a python package ,PrettyTable is a class
# pypi is a website where we can find the packages
table=PrettyTable() # table is the object created from the class PrettyTable

table.add_column("name",["aparna","bhavani","charan"]) # add_column is a method associated with the object table
table.add_column("age",[21,24,27])
print(table.align) # align is an attribute of the object table and it is not a method
print(table)
table.align="l"  # l aligns to the left.    
print(table)









