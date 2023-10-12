import pandas as pd
patriots_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/ne/new-england-patriots'

patriots_2023_tables = pd.read_html(patriots_2023_url)

patriots_2023_off_roster = patriots_2023_tables[0]
print ("Offense")
print(patriots_2023_off_roster)
patriots_2023_off_roster.to_csv("patriots_2023_off_roster.csv")


patriots_2023_def_roster = patriots_2023_tables[1]
print ("Defense")
print(patriots_2023_def_roster)
patriots_2023_def_roster.to_csv("patriots_2023_def_roster.csv")


patriots_2023_st_roster = patriots_2023_tables[2]
print ("Speical Teams")
print(patriots_2023_st_roster)
patriots_2023_st_roster.to_csv("patriots_2023_st_roster.csv")
