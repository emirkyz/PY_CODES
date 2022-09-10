import pandas as pd


data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels_count)

red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)



new_data_dict  = {
    "Fur Color" : ["Grey","Cinnamon","Black"],
    "Count" : [gray_squirrels_count,red_squirrels_count,black_squirrels_count]    
}

new_data = pd.DataFrame(new_data_dict,index=[1,2,3])
new_data.to_csv("Squirrel_count.csv")
print(new_data)