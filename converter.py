import pandas as pd
from datetime import datetime


def get_data():
    data = pd.read_csv("currency.csv")
    return data


def get_ratio(frm, to):
    try:
        return float(to.one_dollar) / float(frm.one_dollar)
    except ZeroDivisionError:
        print("From currency cannot be zero. Error in database\n")


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
    for _ in infile:
        countlines += 1
    infile.close()
    return countlines


def main():
    print("--------------------Welcome to THe converter app--------------------")
    print("--------------------------Press 1 to enter--------------------------")
    choice_1 = int(input())

    if choice_1 == 1:
        print("------------------Which converter You want to use?------------------")
        print("1. For Currency Converter\n2. For Temperature Converter")
        choice_2 = int(input())

        if choice_2 == 1:
            print("Chose the the currency which you want to convert\n1.inr 2.yen 3.yuan 4.euro 5.aud 6.nzd 7.dhiram "
                  "8.riyal ")
            frm = input()
            print("Chose the the currency which you want to converted to\n1.inr 2.yen 3.yuan 4.euro 5.aud 6.nzd "
                  "7.dhiram "
                  "8.riyal ")
            to = input()
            data = get_data()
            print(get_currency(data, frm, to))

        elif choice_2 == 2:
            print("Chose the option\n1. Fahrenheit to celsius\n2. Celsius to fahrenheit\n3. See the logs")
            choice_3 = int(input())

            if choice_3 == 1:
                fahrenheit = float(input("Enter temperature in fahrenheit:\n"))
                print("Temperature in celsius is: " + str(to_celsius(fahrenheit)))

            elif choice_3 == 2:
                celsius = float(input("Enter temperature in celsius:\n"))
                print("Temperature in celsius is: " + str(to_fahrenheit(celsius)))

            elif choice_3 == 3:
                show_temp_file()
                print("Total conversion: " + str(count_lines()))

            else:
                print("Wrong input!")

    else:
        print("---------------------------Thank you!-------------------------------")


if __name__ == "__main__":
    main()
