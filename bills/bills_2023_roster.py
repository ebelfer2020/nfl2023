import pandas as pd
bills_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/buf/buffalo-bills'

bills_2023_tables = pd.read_html(bills_2023_url)

bills_2023_off_roster = bills_2023_tables[0]
print ("Offense")
print(bills_2023_off_roster)
bills_2023_off_roster.to_csv("bills_2023_off_roster.csv")


bills_2023_def_roster = bills_2023_tables[1]
print ("Defense")
print(bills_2023_def_roster)
bills_2023_def_roster.to_csv("bills_2023_def_roster.csv")


bills_2023_st_roster = bills_2023_tables[2]
print ("Speical Teams")
print(bills_2023_st_roster)
bills_2023_st_roster.to_csv("bills_2023_st_roster.csv")
