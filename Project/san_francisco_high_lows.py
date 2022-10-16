import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = "C:\\Users\\damde\\OneDrive\\Pulpit\\ehmatthes-pcc_2e-1.1-2-g078318e\\ehmatthes-pcc_2e-078318e\\chapter_16\\the_csv_file_format\\data\\San Francisco 2018.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    print(header_row)
    # 4, 5
    highs, lows, dates = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[3])
            low = int(row[4])
        except:
            print(f"Nie udało się pobrać danych z dnia {current_date}")
        else:            
            highs.append(high)
            lows.append(low)
            dates.append(current_date)


    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha = 0.5)
    ax.plot(dates, lows, c="blue", alpha = 0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha = 0.1)

    ax.set_title("Najwyższa i najniższa temperatura dnia 2018", fontsize=24)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperatura [F]", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=16)
    
    plt.show()


