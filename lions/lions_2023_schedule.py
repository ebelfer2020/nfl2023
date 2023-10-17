import pandas as pd
lions_2023_url = 'https://en.wikipedia.org/wiki/2023_Detroit_Lions_season'

lions_2023_tables = pd.read_html(lions_2023_url)
lions_2023_schedule = lions_2023_tables[9]
print(lions_2023_schedule)
lions_2023_schedule.to_csv("~/nfl2023/lions/lions_2023_schedule.csv")
