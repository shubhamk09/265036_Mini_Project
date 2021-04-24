import pandas as pd


def get_data():
    data = pd.read_csv("currency.csv")
    return data


def convert_currency(data, from_currency, to_currency):
    frm = data.iloc[data.index[data["name"] == from_currency]]
    to = data.iloc[data.index[data["name"] == to_currency]]

    print(frm)
    print(to)
    return data


data = get_data()
print(convert_currency(data, "inr", "yen"))
