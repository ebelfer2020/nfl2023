import pandas as pd
chargers_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/lac/los-angeles-chargers'

chargers_2023_tables = pd.read_html(chargers_2023_url)

chargers_2023_off_roster = chargers_2023_tables[0]
print ("Offense")
print(chargers_2023_off_roster)
chargers_2023_off_roster.to_csv("chargers_2023_off_roster.csv")


chargers_2023_def_roster = chargers_2023_tables[1]
print ("Defense")
print(chargers_2023_def_roster)
chargers_2023_def_roster.to_csv("chargers_2023_def_roster.csv")


chargers_2023_st_roster = chargers_2023_tables[2]
print ("Speical Teams")
print(chargers_2023_st_roster)
chargers_2023_st_roster.to_csv("chargers_2023_st_roster.csv")
