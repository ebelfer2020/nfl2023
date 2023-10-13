import pandas as pd
saints_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/no/new-orleans-saints'

saints_2023_tables = pd.read_html(saints_2023_url)

saints_2023_off_roster = saints_2023_tables[0]
print ("Offense")
print(saints_2023_off_roster)
saints_2023_off_roster.to_csv("saints_2023_off_roster.csv")


saints_2023_def_roster = saints_2023_tables[1]
print ("Defense")
print(saints_2023_def_roster)
saints_2023_def_roster.to_csv("saints_2023_def_roster.csv")


saints_2023_st_roster = saints_2023_tables[2]
print ("Speical Teams")
print(saints_2023_st_roster)
saints_2023_st_roster.to_csv("saints_2023_st_roster.csv")
