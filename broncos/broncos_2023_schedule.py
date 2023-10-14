import pandas as pd
broncos_2023_url = 'https://en.wikipedia.org/wiki/2023_Denver_Broncos_season'

broncos_2023_tables = pd.read_html(broncos_2023_url)
broncos_2023_schedule = broncos_2023_tables[13]
print(broncos_2023_schedule)
broncos_2023_schedule.to_csv("broncos_2023_schedule.csv")
