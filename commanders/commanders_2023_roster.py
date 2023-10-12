import pandas as pd
commanders_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/wsh/washington-commanders'

commanders_2023_tables = pd.read_html(commanders_2023_url)

commanders_2023_off_roster = commanders_2023_tables[0]
print ("Offense")
print(commanders_2023_off_roster)
commanders_2023_off_roster.to_csv("commanders_2023_off_roster.csv")


commanders_2023_def_roster = commanders_2023_tables[1]
print ("Defense")
print(commanders_2023_def_roster)
commanders_2023_def_roster.to_csv("commanders_2023_def_roster.csv")


commanders_2023_st_roster = commanders_2023_tables[2]
print ("Speical Teams")
print(commanders_2023_st_roster)
commanders_2023_st_roster.to_csv("commanders_2023_st_roster.csv")
