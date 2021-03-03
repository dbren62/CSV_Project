#include all data for 2018
#change title to Daily high and low temps - 2018
#plot low temps too
#shade in the area between high and low

import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")
open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file2 = csv.reader(open_file2, delimiter=",")


header_row = next(csv_file)
header_row2 = next(csv_file2)

#sitka
for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []

lows = []

dates = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date=datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(converted_date)

print(highs)

#death valley
for index, column_header in enumerate(header_row2):
    print("Index:", index, "Column Name:", column_header)

highs2 = []

lows2 = []

dates2 = []

for row in csv_file2:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date=datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        highs2.append(int(row[4]))
        lows2.append(int(row[5]))
        dates2.append(converted_date)

import matplotlib.pyplot as plt
"""
fig=plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=.1)

plt.title("Daily High and Low Temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()
"""
#matplotlib has function called subplots()

fig2, a=plt.subplots(2)

plt.suptitle("Temperature Comparison Between Sitka Airport, AK US and Death Valley, CA US", fontsize=16)
a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="blue")
a[0].fill_between(dates, highs, lows, facecolor="blue", alpha=.1)
a[0].set_title("Sitka, AK US")

a[1].plot(dates2, highs2, c="red")
a[1].plot(dates2, lows2, c="blue")
a[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=.1)
a[1].set_title("Death Valley, CA US")


fig2.autofmt_xdate()

plt.show()