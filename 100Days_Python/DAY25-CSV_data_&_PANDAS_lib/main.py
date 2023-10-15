import pandas
# reading the file into a data frame
data=pandas.read_csv("C:\\vishnu MY Place\\100Days_Python\\DAY25\\weather_data.csv")
# pritning the data frame into which the file is read
print(data)
# printing the columns in the data frame , separately

print(data["temp"])
print(data["day"])
print(data["condition"])

"""we can also use another syntax to print a column/series

print(data.day)
print(data.temp)
print(data.condition)

"""

# now lets check the type of the variable to which the csv file is read
print(type(data)) # SO we can check thast data is a data frame here

# converting the data frame into dictionary
data_dict=data.to_dict()
print(data_dict) #print the dictionary created

#converting a column series into a python list
temp_list=data["temp"].to_list()
print(temp_list)# now we can do all the things whichn can be done wiht pyhton lists
# length of list
print(len(temp_list))
# avg of the temp list(series column)
avg_temp=data["temp"].mean()
print(round(avg_temp,2))
"""
not just the mean , we can find the median,mode , kurtosis etc....
https://pandas.pydata.org/docs/reference/api/pandas.Series.html#main-content
"""
# similarly, finding the max value in a series
max_temp=data.temp.max() # another syntax to refer the column series.
print(max_temp)

# to get a particular row form the data frame

print(data[data.day=="Monday"])

print(data[data.temp==data.temp.max()])

# to get a particular cell /record  in a column/field
monday=data[data.day=="Monday"]
print(monday.condition) # this prints only the condition cell of the monday

monday_temp=monday.temp
monday_temp_F=monday_temp*9/5 +32
print(monday_temp_F)

# creating a data frame
data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data=pandas.DataFrame(data_dict)
#writing the data frame to a csv
data.to_csv("new_data.csv")
