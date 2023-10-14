import pandas as pd
dolphins_2023_url = 'https://en.wikipedia.org/wiki/2023_Miami_Dolphins_season'

dolphins_2023_tables = pd.read_html(dolphins_2023_url)
dolphins_2023_schedule = dolphins_2023_tables[7]
print(dolphins_2023_schedule)
dolphins_2023_schedule.to_csv("dolphins_2023_schedule.csv")
