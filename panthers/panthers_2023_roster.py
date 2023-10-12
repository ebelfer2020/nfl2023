import pandas as pd
panthers_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/car/carolina-panthers'

panthers_2023_tables = pd.read_html(panthers_2023_url)

panthers_2023_off_roster = panthers_2023_tables[0]
print ("Offense")
print(panthers_2023_off_roster)
panthers_2023_off_roster.to_csv("panthers_2023_off_roster.csv")


panthers_2023_def_roster = panthers_2023_tables[1]
print ("Defense")
print(panthers_2023_def_roster)
panthers_2023_def_roster.to_csv("panthers_2023_def_roster.csv")


panthers_2023_st_roster = panthers_2023_tables[2]
print ("Speical Teams")
print(panthers_2023_st_roster)
panthers_2023_st_roster.to_csv("panthers_2023_st_roster.csv")
