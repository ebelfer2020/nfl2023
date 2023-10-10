import pandas as pd
jaguars_2023_url = 'https://en.wikipedia.org/wiki/2023_Jacksonville_Jaguars_season'

jaguars_2023_tables = pd.read_html(jaguars_2023_url)
jaguars_2023_schedule = jaguars_2023_tables[6]
print(jaguars_2023_schedule)
jaguars_2023_schedule.to_csv("jaguarsschedule2023.csv")
