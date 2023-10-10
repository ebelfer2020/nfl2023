import pandas as pd
commanders_2023_url = 'https://en.wikipedia.org/wiki/2023_Washington_Commanders_season'

commanders_2023_tables = pd.read_html(commanders_2023_url)
commanders_2023_schedule = commanders_2023_tables[6]
print(commanders_2023_schedule)
commanders_2023_schedule.to_csv("commandersschedule2023.csv")
