import pandas as pd
browns_2023_url = 'https://en.wikipedia.org/wiki/2023_Cleveland_Browns_season'

browns_2023_tables = pd.read_html(browns_2023_url)
browns_2023_schedule = browns_2023_tables[9]
print(browns_2023_schedule)
browns_2023_schedule.to_csv("brownsschedule2023.csv")
