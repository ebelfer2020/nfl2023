import pandas as pd
saints_2023_url = 'https://en.wikipedia.org/wiki/2023_New_Orleans_Saints_season'

saints_2023_tables = pd.read_html(saints_2023_url)
saints_2023_schedule = saints_2023_tables[6]
print(saints_2023_schedule)
saints_2023_schedule.to_csv("~/nfl2023/saints/saints_2023_schedule.csv")
