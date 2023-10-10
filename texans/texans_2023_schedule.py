import pandas as pd
texans_2023_url = 'https://en.wikipedia.org/wiki/2023_Houston_Texans_season'

texans_2023_tables = pd.read_html(texans_2023_url)
texans_2023_schedule = texans_2023_tables[6]
print(texans_2023_schedule)
texans_2023_schedule.to_csv("texansschedule2023.csv")
