import pandas as pd
colts_2023_url = 'https://en.wikipedia.org/wiki/2023_Indianapolis_Colts_season'

colts_2023_tables = pd.read_html(colts_2023_url)
colts_2023_schedule = colts_2023_tables[6]
print(colts_2023_schedule)
colts_2023_schedule.to_csv("colts_2023_schedule.csv")
