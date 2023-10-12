import pandas as pd
vikings_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/min/minnesota-vikings'

vikings_2023_tables = pd.read_html(vikings_2023_url)

vikings_2023_off_roster = vikings_2023_tables[0]
print ("Offense")
print(vikings_2023_off_roster)
vikings_2023_off_roster.to_csv("vikings_2023_off_roster.csv")


vikings_2023_def_roster = vikings_2023_tables[1]
print ("Defense")
print(vikings_2023_def_roster)
vikings_2023_def_roster.to_csv("vikings_2023_def_roster.csv")


vikings_2023_st_roster = vikings_2023_tables[2]
print ("Speical Teams")
print(vikings_2023_st_roster)
vikings_2023_st_roster.to_csv("vikings_2023_st_roster.csv")
