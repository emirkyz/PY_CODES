from calendar import MONDAY, day_abbr
from msilib.schema import Condition
import pandas as pd
import csv


# with open("./weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)


data = pd.read_csv("./weather_data.csv")

# print(data["temp"])


temp_list = data["temp"].to_list()
#print(temp_list)


#print(data["temp"].mean())


#print(data["temp"].max())



# print(data["condition"])
# print(data.condition)


#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])



# monday = data[data.day == "Monday"]
# print(monday.condition)


#### creating data frame 

data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [75,56,65]
}

data = pd.DataFrame(data_dict,index=["1","2","3"])
print(data)

