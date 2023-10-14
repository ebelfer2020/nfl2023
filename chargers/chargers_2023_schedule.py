import pandas as pd
chargers_2023_url = 'https://en.wikipedia.org/wiki/2023_Los_Angeles_Chargers_season'

chargers_2023_tables = pd.read_html(chargers_2023_url)
chargers_2023_schedule = chargers_2023_tables[18]
print(chargers_2023_schedule)
chargers_2023_schedule.to_csv("chargers_2023_schedule.csv")
