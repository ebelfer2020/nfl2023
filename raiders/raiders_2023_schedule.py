import pandas as pd
raiders_2023_url = 'https://en.wikipedia.org/wiki/2023_Las_Vegas_Raiders_season'

raiders_2023_tables = pd.read_html(raiders_2023_url)
raiders_2023_schedule = raiders_2023_tables[9]
print(raiders_2023_schedule)
raiders_2023_schedule.to_csv("~/nfl2023/raiders/raiders_2023_schedule.csv")
