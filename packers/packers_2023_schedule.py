import pandas as pd
packers_2023_url = 'https://en.wikipedia.org/wiki/2023_Green_Bay_Packers_season'

packers_2023_tables = pd.read_html(packers_2023_url)
packers_2023_schedule = packers_2023_tables[12]
print(packers_2023_schedule)
packers_2023_schedule.to_csv("packersschedule2023.csv")
