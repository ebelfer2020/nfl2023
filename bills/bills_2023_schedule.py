import pandas as pd
bills_2023_url = 'https://en.wikipedia.org/wiki/2023_Buffalo_Bills_season'

bills_2023_tables = pd.read_html(bills_2023_url)
bills_2023_schedule = bills_2023_tables[9]
print(bills_2023_schedule)
bills_2023_schedule.to_csv("billsschedule2023.csv")
