import pandas as pd
chiefs_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/kc/kansas-city-chiefs'


chiefs_2023_tables = pd.read_html(chiefs_2023_url)

chiefs_2023_off_roster = chiefs_2023_tables[0]
print ("Offense")
print(chiefs_2023_off_roster)
chiefs_2023_off_roster.to_csv("chiefs_2023_off_roster.csv")


chiefs_2023_def_roster = chiefs_2023_tables[1]
print ("Defense")
print(chiefs_2023_def_roster)
chiefs_2023_def_roster.to_csv("chiefs_2023_def_roster.csv")


chiefs_2023_st_roster = chiefs_2023_tables[2]
print ("Speical Teams")
print(chiefs_2023_st_roster)
chiefs_2023_st_roster.to_csv("chiefs_2023_st_roster.csv")
