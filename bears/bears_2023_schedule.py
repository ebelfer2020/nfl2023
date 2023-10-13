import pandas as pd
bears_2023_url = 'https://en.wikipedia.org/wiki/2023_Chicago_Bears_season'

bears_2023_tables = pd.read_html(bears_2023_url)
bears_2023_schedule = bears_2023_tables[6]
print(bears_2023_schedule)
bears_2023_schedule.to_csv("bears_2023_schedule.csv")
