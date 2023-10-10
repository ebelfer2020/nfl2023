import pandas as pd
giants_2023_url = 'https://en.wikipedia.org/wiki/2023_New_York_Giants_season'

giants_2023_tables = pd.read_html(giants_2023_url)
giants_2023_schedule = giants_2023_tables[11]
print(giants_2023_schedule)
giants_2023_schedule.to_csv("giantsschedule2023.csv")
