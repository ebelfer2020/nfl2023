import pandas as pd
bengals_2023_url = 'https://en.wikipedia.org/wiki/2023_Cincinnati_Bengals_season'

bengals_2023_tables = pd.read_html(bengals_2023_url)
bengals_2023_schedule = bengals_2023_tables[10]
print(bengals_2023_schedule)
bengals_2023_schedule.to_csv("bengalsschedule2023.csv")
