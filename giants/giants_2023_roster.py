import pandas as pd
giants_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/nyg/new-york-giants'

giants_2023_tables = pd.read_html(giants_2023_url)

giants_2023_off_roster = giants_2023_tables[0]
print ("Offense")
print(giants_2023_off_roster)
giants_2023_off_roster.to_csv("giants_2023_off_roster.csv")


giants_2023_def_roster = giants_2023_tables[1]
print ("Defense")
print(giants_2023_def_roster)
giants_2023_def_roster.to_csv("giants_2023_def_roster.csv")


giants_2023_st_roster = giants_2023_tables[2]
print ("Speical Teams")
print(giants_2023_st_roster)
giants_2023_st_roster.to_csv("giants_2023_st_roster.csv")
