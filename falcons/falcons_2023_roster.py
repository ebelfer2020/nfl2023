import pandas as pd
falcons_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/atl/atlanta-falcons'

falcons_2023_tables = pd.read_html(falcons_2023_url)

falcons_2023_off_roster = falcons_2023_tables[0]
print ("Offense")
print(falcons_2023_off_roster)
falcons_2023_off_roster.to_csv("falcons_2023_off_roster.csv")


falcons_2023_def_roster = falcons_2023_tables[1]
print ("Defense")
print(falcons_2023_def_roster)
falcons_2023_def_roster.to_csv("falcons_2023_def_roster.csv")


falcons_2023_st_roster = falcons_2023_tables[2]
print ("Speical Teams")
print(falcons_2023_st_roster)
falcons_2023_st_roster.to_csv("falcons_2023_st_roster.csv")
