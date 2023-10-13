import pandas as pd
broncos_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/den/denver-broncos'

broncos_2023_tables = pd.read_html(broncos_2023_url)

broncos_2023_off_roster = broncos_2023_tables[0]
print ("Offense")
print(broncos_2023_off_roster)
broncos_2023_off_roster.to_csv("broncos_2023_off_roster.csv")


broncos_2023_def_roster = broncos_2023_tables[1]
print ("Defense")
print(broncos_2023_def_roster)
broncos_2023_def_roster.to_csv("broncos_2023_def_roster.csv")


broncos_2023_st_roster = broncos_2023_tables[2]
print ("Speical Teams")
print(broncos_2023_st_roster)
broncos_2023_st_roster.to_csv("broncos_2023_st_roster.csv")
