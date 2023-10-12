import pandas as pd
cowboys_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/dal/dallas-cowboys:'

cowboys_2023_tables = pd.read_html(cowboys_2023_url)

cowboys_2023_off_roster = cowboys_2023_tables[0]
print ("Offense")
print(cowboys_2023_off_roster)
cowboys_2023_off_roster.to_csv("cowboys_2023_off_roster.csv")


cowboys_2023_def_roster = cowboys_2023_tables[1]
print ("Defense")
print(cowboys_2023_def_roster)
cowboys_2023_def_roster.to_csv("cowboys_2023_def_roster.csv")


cowboys_2023_st_roster = cowboys_2023_tables[2]
print ("Speical Teams")
print(cowboys_2023_st_roster)
cowboys_2023_st_roster.to_csv("cowboys_2023_st_roster.csv")
