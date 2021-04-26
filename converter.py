import pandas as pd
from datetime import datetime


def get_data():
    data = pd.read_csv("currency.csv")
    return data


def get_ratio(frm, to):
    return float(frm.one_dollar) / float(to.one_dollar)


def convert(frm, to):
    convert_ratio = get_ratio(frm, to)
    number = float(input("Enter the amount you want to convert:\n"))
    return convert_ratio * number


def get_currency(data, from_currency, to_currency):
    frm = data.iloc[data.index[data["name"] == from_currency]]
    to = data.iloc[data.index[data["name"] == to_currency]]
    return convert(frm, to)


def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    write_temp_to_file(fahrenheit, celsius, "FtoC")
    return celsius


def to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    write_temp_to_file(celsius, fahrenheit, "CtoF")
    return fahrenheit


def write_temp_to_file(frm, to, tp):
    outfile = open("temperature_record.txt", "a")
    now = datetime.now()
    outfile.write(str(now) + " " + str(frm) + " " + str(to) + " " + str(tp) + "\n")
    outfile.close()


def show_temp_file():
    infile = open("temperature_record.txt", "r")
    line = infile.read()
    print(line)
    infile.close()


def count_lines():
    infile = open("temperature_record.txt", "r")
    countlines = 0
    for line in infile:
        countlines += 1
    infile.close()
    return countlines


data = get_data()
# print(get_currency(data, "inr", "yen"))
# print(to_celsius(99.0))
# print(to_fahrenheit(32.0))
show_temp_file()
print(count_lines())
