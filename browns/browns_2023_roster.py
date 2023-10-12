import pandas as pd
browns_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/cle/cleveland-browns'

browns_2023_tables = pd.read_html(browns_2023_url)

browns_2023_off_roster = browns_2023_tables[0]
print ("Offense")
print(browns_2023_off_roster)
browns_2023_off_roster.to_csv("browns_2023_off_roster.csv")


browns_2023_def_roster = browns_2023_tables[1]
print ("Defense")
print(browns_2023_def_roster)
browns_2023_def_roster.to_csv("browns_2023_def_roster.csv")


browns_2023_st_roster = browns_2023_tables[2]
print ("Speical Teams")
print(browns_2023_st_roster)
browns_2023_st_roster.to_csv("browns_2023_st_roster.csv")
