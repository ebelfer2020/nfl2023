import pandas as pd
rams_2023_url = 'https://en.wikipedia.org/wiki/2023_Los_Angeles_Rams_season'

rams_2023_tables = pd.read_html(rams_2023_url)
rams_2023_schedule = rams_2023_tables[15]
print(rams_2023_schedule)
rams_2023_schedule.to_csv("ramsschedule2023.csv")
