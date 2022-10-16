import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "A:\\Programy\\DataVisualization\\Project\\data\\sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[header_row.index("DATE")], "%Y-%m-%d")
        high = int(row[header_row.index("TMAX")])
        low = int(row[header_row.index("TMIN")])
        highs.append(high)
        dates.append(current_date)
        lows.append(low)





    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    ax.set_title("Najwyższa i najniższa temperatura dnia 2018", fontsize=24)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperatura [F]", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=16)
    ax.set_ylim(20, 135)

    plt.show()