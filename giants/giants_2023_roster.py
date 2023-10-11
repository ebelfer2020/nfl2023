import pandas as pd
eagles_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/phi/philadelphia-eagles'

eagles_2023_tables = pd.read_html(eagles_2023_url)

eagles_2023_off_roster = eagles_2023_tables[0]
print ("Offense")
print(eagles_2023_off_roster)
eagles_2023_off_roster.to_csv("eagles_2023_off_roster.csv")


eagles_2023_def_roster = eagles_2023_tables[1]
print ("Defense")
print(eagles_2023_def_roster)
eagles_2023_def_roster.to_csv("eagles_2023_def_roster.csv")


eagles_2023_st_roster = eagles_2023_tables[2]
print ("Speical Teams")
print(eagles_2023_st_roster)
eagles_2023_st_roster.to_csv("eagles_2023_st_roster.csv")
