import pandas as pd
lions_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/det/detroit-lions'

lions_2023_tables = pd.read_html(lions_2023_url)

lions_2023_off_roster = lions_2023_tables[0]
print ("Offense")
print(lions_2023_off_roster)
lions_2023_off_roster.to_csv("lions_2023_off_roster.csv")


lions_2023_def_roster = lions_2023_tables[1]
print ("Defense")
print(lions_2023_def_roster)
lions_2023_def_roster.to_csv("lions_2023_def_roster.csv")


lions_2023_st_roster = lions_2023_tables[2]
print ("Speical Teams")
print(lions_2023_st_roster)
lions_2023_st_roster.to_csv("lions_2023_st_roster.csv")
