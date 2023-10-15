# A dictionary contains Key and value pairs i.e, key is like the word  and value is like the meaning of the word.
# syntax-----> {key:value}
#each key can only have only one value.
#data types of key and value can be different.

programming_dictionary={
    "Bug":"An error in a program that prevents the program that prevents the program from running as expected.",
    123:"A piece of code that you can call over and over again.", # here the key 123 is declared as integer Data type.
}
# while retrieving the key, the data type must be the  same as the data type as declared in the dectionary.

#retriving items from the dictionary.
print(programming_dictionary["Bug"])     # here , Bug is retrived as a string as it is declared as a string data type in the dictionary.

# adding new items to the dictionary
programming_dictionary["Loop"]="An action of doing something over and over again."

print(programming_dictionary)

# creating an empty dictionary , so that to add items later, as shown in the above method.

empty_dictionary={}

# wipe an exixting dictionary
# programming_dictionary={}

#print(programming_dictionary)

#edit an item in the dictionary

programming_dictionary["Bug"]="A moth in side your computer."

print(programming_dictionary)

#Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
