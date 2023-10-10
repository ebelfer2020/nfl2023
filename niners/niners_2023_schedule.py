import pandas as pd
niners_2023_url = 'https://en.wikipedia.org/wiki/2023_San_Francisco_49ers_season'

niners_2023_tables = pd.read_html(niners_2023_url)
niners_2023_schedule = niners_2023_tables[10]
print(niners_2023_schedule)
niners_2023_schedule.to_csv("ninersschedule2023.csv")
