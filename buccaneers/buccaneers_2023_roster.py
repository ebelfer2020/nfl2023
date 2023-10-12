import pandas as pd
buccaneers_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/tb/tampa-bay-buccaneers'

buccaneers_2023_tables = pd.read_html(buccaneers_2023_url)

buccaneers_2023_off_roster = buccaneers_2023_tables[0]
print ("Offense")
print(buccaneers_2023_off_roster)
buccaneers_2023_off_roster.to_csv("buccaneers_2023_off_roster.csv")


buccaneers_2023_def_roster = buccaneers_2023_tables[1]
print ("Defense")
print(buccaneers_2023_def_roster)
buccaneers_2023_def_roster.to_csv("buccaneers_2023_def_roster.csv")


buccaneers_2023_st_roster = buccaneers_2023_tables[2]
print ("Speical Teams")
print(buccaneers_2023_st_roster)
buccaneers_2023_st_roster.to_csv("buccaneers_2023_st_roster.csv")
