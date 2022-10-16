import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime


filename = "A:\\Programy\\DataVisualization\\Project\\data\\world_fires_1_day.csv"
title = "Fire in World"

with open(filename) as f:
    all_fire_data = csv.reader(f)
    header_row = next(all_fire_data)

    lons, lats, brightnesses, dates = [], [], [], []

    for row in all_fire_data:
        lon = float(row[header_row.index("longitude")])
        lat = float(row[header_row.index("latitude")])
        #brightness = float(row[header_row.index('brightness')])
        brightness = float(row[header_row.index("brightness")])
        current_date = datetime.strptime(row[header_row.index('acq_date')], "%Y-%m-%d")

        lons.append(lon)
        lats.append(lat)
        brightnesses.append(brightness)
        dates.append(current_date)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates,
    }]

my_layout = Layout(title=title)

fig = {'data': data, 'layout' : my_layout}
offline.plot(fig, filename="global_fires.html")