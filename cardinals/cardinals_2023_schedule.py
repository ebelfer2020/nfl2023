import pandas as pd
cardinals_2023_url = 'https://en.wikipedia.org/wiki/2023_Arizona_Cardinals_season'

cardinals_2023_tables = pd.read_html(cardinals_2023_url)
cardinals_2023_schedule = cardinals_2023_tables[8]
print(cardinals_2023_schedule)
cardinals_2023_schedule.to_csv("cardinals_2023_schedule.csv")
