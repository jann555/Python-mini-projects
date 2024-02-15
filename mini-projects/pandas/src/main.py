import pandas as pd

data = pd.read_csv('../resources/weather_data.csv')
# temperatures = [int(datum[1]) for datum in data if datum[1] != 'temp']
# Get data in columns
data_dict = data.to_dict()
print(data_dict)
temperatures = data.temp.max()

print(f'Average Temperatures: {format(temperatures, ".2f")} Celcius')


def celcius_to_farenh(temp):
    return temp * 9 / 5 + 32


# Get data in rows
sunday = data[data.temp == data.temp.max()]
print(sunday)
tuesday = data[data.day == "Tuesday"].temp
print(celcius_to_farenh(tuesday))

# Create Dataframe from scratch

data_dict_sample = {
    "students": ["Rodolfo", "Patricio", "Katia"],
    "scores": [85, 98, 92]
}

data = pd.DataFrame(data_dict_sample)
data.to_csv("../resources/new_data.csv")

