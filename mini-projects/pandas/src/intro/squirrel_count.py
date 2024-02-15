import pandas as pd

squirrel_data = pd.read_csv(
    '../../resources/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240213.csv')

gray_sq = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cnnmn_sq = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
blck_sq = len(squirrel_data[squirrel_data["Primary Fur Color"] == "black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq, cnnmn_sq, blck_sq]
}

data = pd.DataFrame(data_dict)
data.to_csv("../resources/short-list-squirrels.csv")


