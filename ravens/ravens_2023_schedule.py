import pandas as pd
ravens_2023_url = 'https://en.wikipedia.org/wiki/2023_Baltimore_Ravens_season'

ravens_2023_tables = pd.read_html(ravens_2023_url)
ravens_2023_schedule = ravens_2023_tables[11]
print(ravens_2023_schedule)
ravens_2023_schedule.to_csv("ravensschedule2023.csv")
