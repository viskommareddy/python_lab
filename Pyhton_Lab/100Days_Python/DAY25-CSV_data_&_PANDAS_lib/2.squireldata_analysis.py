import pandas
df=pandas.read_csv("C:\\Users\\vishn\\Downloads\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df)
print(df["Primary Fur Color"])
gray_squirells=df[df["Primary Fur Color"]=="Gray"]
print(gray_squirells)
gray_squirells_count=len(df[df["Primary Fur Color"]=="Gray"])
red_squrells_count=len(df[df["Primary Fur Color"]=="Cinnamon"])
black_squirells_count=len(df[df["Primary Fur Color"]=="Black"])
print(gray_squirells_count)
print(red_squrells_count)
print(black_squirells_count)

data_dict={
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirells_count,red_squrells_count,black_squirells_count]
}
data_frame=pandas.DataFrame(data_dict)
data_frame.to_csv("squirell_count.csv")
