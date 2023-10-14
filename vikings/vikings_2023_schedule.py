import pandas as pd
vikings_2023_url = 'https://en.wikipedia.org/wiki/2023_Minnesota_Vikings_season'

vikings_2023_tables = pd.read_html(vikings_2023_url)
vikings_2023_schedule = vikings_2023_tables[17]
print(vikings_2023_schedule)
vikings_2023_schedule.to_csv("vikings_2023_schedule.csv")
