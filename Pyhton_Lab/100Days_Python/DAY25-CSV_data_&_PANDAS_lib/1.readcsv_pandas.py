import pandas #importing the pandas (for dat analysis)
#reading A CSV INTO A DATA FRAME
data=pandas.read_csv("C:\\Users\\vishn\\Downloads\\weather_data.csv")
#printing the data frame
print(data)
#printing a column
print(data["temp"])
#type of the data is dataframe
print(type(data))
#type of temp column is series
print(type(data["temp"]))
#coverting the data frame to a dictionary 
data_dict=data.to_dict
print(data_dict)
#converting the temp column inot a list
temp_list=data["temp"].to_list
print(temp_list)
print(type(temp_list))
day_list=data["day"].to_list
print(day_list)
print(type(day_list))
# average of temp column
print(data["temp"].mean())
# max value of temp column
print( data["temp"].max())
#another method of selecting the column
print(data.day)
print(data.temp)
print(data.condition)
#get data in a row
print(data[data.day=="Monday"])
#get the row with max temp
print(data[data.temp==data.temp.max()])
#get the condition corresponding to monday alone
monday=data[data.day=="Monday"]
print(monday.condition)
#converting the temp on monday to F
monday_temp=monday.temp[0]
monday_temp_F=monday_temp*(9/5)+32
print(monday_temp_F)
#creaitng a dataframe from scratch 
data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_temp.csv")