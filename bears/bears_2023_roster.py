import pandas as pd
bears_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/chi/chicago-bears'

bears_2023_tables = pd.read_html(bears_2023_url)

bears_2023_off_roster = bears_2023_tables[0]
print ("Offense")
print(bears_2023_off_roster)
bears_2023_off_roster.to_csv("bears_2023_off_roster.csv")


bears_2023_def_roster = bears_2023_tables[1]
print ("Defense")
print(bears_2023_def_roster)
bears_2023_def_roster.to_csv("bears_2023_def_roster.csv")


bears_2023_st_roster = bears_2023_tables[2]
print ("Speical Teams")
print(bears_2023_st_roster)
bears_2023_st_roster.to_csv("bears_2023_st_roster.csv")
