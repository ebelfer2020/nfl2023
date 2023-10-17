import pandas as pd
cowboys_2023_url = 'https://en.wikipedia.org/wiki/2023_Dallas_Cowboys_season'

cowboys_2023_tables = pd.read_html(cowboys_2023_url)
cowboys_2023_schedule = cowboys_2023_tables[10]
print(cowboys_2023_schedule)
cowboys_2023_schedule.to_csv("~/nfl2023/cowboys/cowboys_2023_schedule.csv")
