import pandas as pd
jets_2023_url = 'https://en.wikipedia.org/wiki/2023_New_York_Jets_season'

jets_2023_tables = pd.read_html(jets_2023_url)
jets_2023_schedule = jets_2023_tables[6]
print(jets_2023_schedule)
jets_2023_schedule.to_csv("jetsschedule2023.csv")
