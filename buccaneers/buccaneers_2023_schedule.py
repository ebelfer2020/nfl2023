import pandas as pd
buccaneers_2023_url = 'https://en.wikipedia.org/wiki/2023_Tampa_Bay_Buccaneers_season'

buccaneers_2023_tables = pd.read_html(buccaneers_2023_url)
buccaneers_2023_schedule = buccaneers_2023_tables[6]
print(buccaneers_2023_schedule)
buccaneers_2023_schedule.to_csv("buccaneers_2023_schedule.csv")
