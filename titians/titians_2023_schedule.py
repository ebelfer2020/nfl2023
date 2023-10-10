import pandas as pd
titians_2023_url = 'https://en.wikipedia.org/wiki/2023_Tennessee_Titans_season'

titians_2023_tables = pd.read_html(titians_2023_url)
titians_2023_schedule = titians_2023_tables[7]
print(titians_2023_schedule)
titians_2023_schedule.to_csv("titiansschedule2023.csv")
