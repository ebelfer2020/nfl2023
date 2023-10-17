import pandas as pd
seahawks_2023_url = 'https://en.wikipedia.org/wiki/2023_Seattle_Seahawks_season'

seahawks_2023_tables = pd.read_html(seahawks_2023_url)
seahawks_2023_schedule = seahawks_2023_tables[9]
print(seahawks_2023_schedule)
seahawks_2023_schedule.to_csv("~/nfl2023/seahawks/seahawks_2023_schedule.csv")
