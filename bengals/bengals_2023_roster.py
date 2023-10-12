import pandas as pd
bengals_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/cin/cincinnati-bengals'

bengals_2023_tables = pd.read_html(bengals_2023_url)

bengals_2023_off_roster = bengals_2023_tables[0]
print ("Offense")
print(bengals_2023_off_roster)
bengals_2023_off_roster.to_csv("bengals_2023_off_roster.csv")


bengals_2023_def_roster = bengals_2023_tables[1]
print ("Defense")
print(bengals_2023_def_roster)
bengals_2023_def_roster.to_csv("bengals_2023_def_roster.csv")


bengals_2023_st_roster = bengals_2023_tables[2]
print ("Speical Teams")
print(bengals_2023_st_roster)
bengals_2023_st_roster.to_csv("bengals_2023_st_roster.csv")
