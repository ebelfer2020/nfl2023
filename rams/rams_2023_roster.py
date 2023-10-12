import pandas as pd
rams_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/lar/los-angeles-rams'

rams_2023_tables = pd.read_html(rams_2023_url)

rams_2023_off_roster = rams_2023_tables[0]
print ("Offense")
print(rams_2023_off_roster)
rams_2023_off_roster.to_csv("rams_2023_off_roster.csv")


rams_2023_def_roster = rams_2023_tables[1]
print ("Defense")
print(rams_2023_def_roster)
rams_2023_def_roster.to_csv("rams_2023_def_roster.csv")


rams_2023_st_roster = rams_2023_tables[2]
print ("Speical Teams")
print(rams_2023_st_roster)
rams_2023_st_roster.to_csv("rams_2023_st_roster.csv")
