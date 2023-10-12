import pandas as pd
dolphins_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/mia/miami-dolphins'

dolphins_2023_tables = pd.read_html(dolphins_2023_url)

dolphins_2023_off_roster = dolphins_2023_tables[0]
print ("Offense")
print(dolphins_2023_off_roster)
dolphins_2023_off_roster.to_csv("dolphins_2023_off_roster.csv")


dolphins_2023_def_roster = dolphins_2023_tables[1]
print ("Defense")
print(dolphins_2023_def_roster)
dolphins_2023_def_roster.to_csv("dolphins_2023_def_roster.csv")


dolphins_2023_st_roster = dolphins_2023_tables[2]
print ("Speical Teams")
print(dolphins_2023_st_roster)
dolphins_2023_st_roster.to_csv("dolphins_2023_st_roster.csv")
