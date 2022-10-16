import csv
from datetime import datetime
from tokenize import Double
import matplotlib.pyplot as plt

filename = "A:\\Programy\\DataVisualization\\Project\\data\\sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print (header_row)

    rainings, dates = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            daily_raining = float(row[3])
        except ValueError:
            print(f"Brak danych dla {current_date}")
        else:
            dates.append(current_date)
            rainings.append(daily_raining)

    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(dates, rainings, c="blue", alpha=0.5)

    title = "Opady deszczu \nSitka"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    ax.set_title("Wielkośc opadów deszczu w Sitka", fontsize=24)
    ax.set_xlabel("", fontsize=26)
    fig.autofmt_xdate()
    ax.set_ylabel("Wielkośc opadów", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=16)

    plt.show()