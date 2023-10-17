import pandas as pd
titans_2023_url = 'https://en.wikipedia.org/wiki/2023_Tennessee_Titans_season'

titans_2023_tables = pd.read_html(titans_2023_url)
titans_2023_schedule = titans_2023_tables[7]
print(titans_2023_schedule)
titans_2023_schedule.to_csv("~/nfl2023/titans/titans_2023_schedule.csv")
