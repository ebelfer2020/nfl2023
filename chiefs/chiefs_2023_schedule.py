import pandas as pd
chiefs_2023_url = 'https://en.wikipedia.org/wiki/2023_Kansas_City_Chiefs_season'

chiefs_2023_tables = pd.read_html(chiefs_2023_url)
chiefs_2023_schedule = chiefs_2023_tables[31]
print(chiefs_2023_schedule)
chiefs_2023_schedule.to_csv("chiefsschedule2023.csv")