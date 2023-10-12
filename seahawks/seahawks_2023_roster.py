import pandas as pd
seahawks_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/sea/seattle-seahawks'

seahawks_2023_tables = pd.read_html(seahawks_2023_url)

seahawks_2023_off_roster = seahawks_2023_tables[0]
print ("Offense")
print(seahawks_2023_off_roster)
seahawks_2023_off_roster.to_csv("seahawks_2023_off_roster.csv")


seahawks_2023_def_roster = seahawks_2023_tables[1]
print ("Defense")
print(seahawks_2023_def_roster)
seahawks_2023_def_roster.to_csv("seahawks_2023_def_roster.csv")


seahawks_2023_st_roster = seahawks_2023_tables[2]
print ("Speical Teams")
print(seahawks_2023_st_roster)
seahawks_2023_st_roster.to_csv("seahawks_2023_st_roster.csv")
