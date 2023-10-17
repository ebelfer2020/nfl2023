import pandas as pd
steelers_2023_url = 'https://en.wikipedia.org/wiki/2023_Pittsburgh_Steelers_season'

steelers_2023_tables = pd.read_html(steelers_2023_url)
steelers_2023_schedule = steelers_2023_tables[6]
print(steelers_2023_schedule)
steelers_2023_schedule.to_csv("~/nfl2023/steelers/steelers_2023_schedule.csv")
