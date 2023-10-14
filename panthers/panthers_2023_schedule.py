import pandas as pd
panthers_2023_url = 'https://en.wikipedia.org/wiki/2023_Carolina_Panthers_season'

panthers_2023_tables = pd.read_html(panthers_2023_url)
panthers_2023_schedule = panthers_2023_tables[6]
print(panthers_2023_schedule)
panthers_2023_schedule.to_csv("panthers_2023_schedule.csv")
