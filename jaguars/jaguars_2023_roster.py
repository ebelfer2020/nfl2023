import pandas as pd
jaguars_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/jax/jacksonville-jaguars'

jaguars_2023_tables = pd.read_html(jaguars_2023_url)

jaguars_2023_off_roster = jaguars_2023_tables[0]
print ("Offense")
print(jaguars_2023_off_roster)
jaguars_2023_off_roster.to_csv("jaguars_2023_off_roster.csv")


jaguars_2023_def_roster = jaguars_2023_tables[1]
print ("Defense")
print(jaguars_2023_def_roster)
jaguars_2023_def_roster.to_csv("jaguars_2023_def_roster.csv")


jaguars_2023_st_roster = jaguars_2023_tables[2]
print ("Speical Teams")
print(jaguars_2023_st_roster)
jaguars_2023_st_roster.to_csv("jaguars_2023_st_roster.csv")
