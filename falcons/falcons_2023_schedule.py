import pandas as pd
falcons_2023_url = 'https://en.wikipedia.org/wiki/2023_Atlanta_Falcons_season'

falcons_2023_tables = pd.read_html(falcons_2023_url)
falcons_2023_schedule = falcons_2023_tables[6]
print(falcons_2023_schedule)
falcons_2023_schedule.to_csv("falconsschedule2023.csv")
