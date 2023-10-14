import pandas as pd
patriots_2023_url = 'https://en.wikipedia.org/wiki/2023_New_England_Patriots_season'

patriots_2023_tables = pd.read_html(patriots_2023_url)
patriots_2023_schedule = patriots_2023_tables[11]
print(patriots_2023_schedule)
patriots_2023_schedule.to_csv("patriots_2023_schedule.csv")
