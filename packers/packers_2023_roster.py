import pandas as pd
packers_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/gb/green-bay-packers'

packers_2023_tables = pd.read_html(packers_2023_url)

packers_2023_off_roster = packers_2023_tables[0]
print ("Offense")
print(packers_2023_off_roster)
packers_2023_off_roster.to_csv("packers_2023_off_roster.csv")


packers_2023_def_roster = packers_2023_tables[1]
print ("Defense")
print(packers_2023_def_roster)
packers_2023_def_roster.to_csv("packers_2023_def_roster.csv")


packers_2023_st_roster = packers_2023_tables[2]
print ("Speical Teams")
print(packers_2023_st_roster)
packers_2023_st_roster.to_csv("packers_2023_st_roster.csv")
