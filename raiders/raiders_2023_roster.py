import pandas as pd
raiders_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/lv/las-vegas-raiders'

raiders_2023_tables = pd.read_html(raiders_2023_url)

raiders_2023_off_roster = raiders_2023_tables[0]
print ("Offense")
print(raiders_2023_off_roster)
raiders_2023_off_roster.to_csv("raiders_2023_off_roster.csv")


raiders_2023_def_roster = raiders_2023_tables[1]
print ("Defense")
print(raiders_2023_def_roster)
raiders_2023_def_roster.to_csv("raiders_2023_def_roster.csv")


raiders_2023_st_roster = raiders_2023_tables[2]
print ("Speical Teams")
print(raiders_2023_st_roster)
raiders_2023_st_roster.to_csv("raiders_2023_st_roster.csv")
